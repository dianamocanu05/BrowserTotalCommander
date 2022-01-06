import os
from src.utils import get_file_by_name


def copy_paste(files, destination, tree):
    for file_name in files:
        file_name = file_name[:-1]
        destination = os.path.join(destination, file_name)
        file = get_file_by_name(file_name, tree)
        file.copy(destination)
