import os
import shutil
from rich.progress import Progress
from .utils import hash_file, load_ignore_patterns, should_ignore


def add_to_store(db_cursor, app_dir, project_id, store_dir, ignore_file=None):
    db_cursor.execute('SELECT * FROM files WHERE project_id = ?', (project_id,))
    if db_cursor.fetchone():
        raise Exception(f"Project with id {project_id} already exists in the database.")

    os.makedirs(store_dir, exist_ok=True)

    if ignore_file is None:
        ignore_file = os.path.join(app_dir, '.titanic-ignore')

    ignore_patterns = load_ignore_patterns(ignore_file)

    all_files = []
    for root, _, files in os.walk(app_dir):
        for file in files:
            filepath = os.path.join(root, file)
            relative_path = os.path.relpath(filepath, app_dir)
            all_files.append((filepath, relative_path))

    with Progress() as progress:
        task = progress.add_task("[green]Adding files to store...", total=len(all_files))

        for filepath, relative_path in all_files:
            if should_ignore(relative_path, ignore_patterns):
                progress.update(task, advance=1)
                continue

            file_hash = hash_file(filepath)
            file_mode = os.stat(filepath).st_mode
            prefix = file_hash[:3]
            store_path = os.path.join(store_dir, prefix, file_hash)

            db_cursor.execute('''
                INSERT INTO files (path, hash, mode, project_id)
                VALUES (?, ?, ?, ?)
            ''', (relative_path, file_hash, file_mode, project_id))

            if not os.path.exists(store_path):
                os.makedirs(os.path.dirname(store_path), exist_ok=True)
                shutil.copy(filepath, store_path)

            progress.update(task, advance=1)


def recreate_from_store(db_cursor, project_id, output_dir, store_dir):
    db_cursor.execute('SELECT * FROM files WHERE project_id = ?', (project_id,))
    files_to_process = db_cursor.fetchall()

    os.makedirs(output_dir, exist_ok=True)

    with Progress() as progress:
        task = progress.add_task("[green]Recreating project from store...", total=len(files_to_process))

        for file_info in files_to_process:
            dest_path = os.path.join(output_dir, file_info[1])
            source_path = os.path.join(store_dir, file_info[2][:3], file_info[2])

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            shutil.copy(source_path, dest_path)

            progress.update(task, advance=1)
