import hashlib
import os
import pathspec


def hash_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()


def load_ignore_patterns(ignore_file):
    patterns = []

    if os.path.exists(ignore_file):
        with open(ignore_file, 'r') as f:
            patterns = [line.strip() for line in f if line.strip() and not line.startswith('#')]

    spec = pathspec.PathSpec.from_lines('gitwildmatch', patterns)
    return spec


def should_ignore(file_path, ignore_spec):
    return ignore_spec.match_file(file_path)
