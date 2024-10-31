import sqlite3
import subprocess


def rsync_with_includes(remote_server, source, destination, includes):
    with open('/tmp/includes.txt', 'w') as f:
        f.write("\n".join(includes))

    include_opt = ["--include-from=/tmp/includes.txt"]
    exclude_opt = ["--exclude=*"]

    rsync_command = ["rsync", "-avz"] + include_opt + exclude_opt + [f"{remote_server}:{source}/", destination]

    result = subprocess.run(rsync_command)
    if result.returncode != 0:
        raise Exception("rsync failed")


def sync_metadata_and_files(local_db_cursor, remote_server, project_id, remote_metadata_path, store_dir, remote_store_dir):
    remote_metadata_clone_path = '/tmp/titanic-metadata.db'

    subprocess.run(["rsync", "-avz", f"{remote_server}:{remote_metadata_path}", remote_metadata_clone_path])

    conn = sqlite3.connect(remote_metadata_clone_path)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM files WHERE project_id = ?', (project_id,))
    except sqlite3.OperationalError:
        print("Project ID not found in remote metadata")
        return False
    files_to_process = cursor.fetchall()

    local_db_cursor.execute('INSERT INTO files (path, hash, mode, project_id) VALUES (?, ?, ?, ?)', files_to_process)

    includes = [file_info[2] for file_info in files_to_process]

    rsync_with_includes(remote_server, remote_store_dir, store_dir, includes)
    return True
