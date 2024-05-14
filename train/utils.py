import os
import sys


def get_repo_path() -> str:
    file_path = sys.argv[0]
    abs_path = os.path.abspath(file_path)
    repo_dir = os.path.dirname(abs_path)
    return repo_dir
