import os
from src.utils import get_file_by_name


def copy_paste(files, destination, tree):
    """
    copy_paste iterates through the files to be copied, gets the corresponding File objects
    and moves the files to the specified destination
    :param files: file names to be copied
    :param destination: destination for the files
    :param tree: the file tree
    :return: nothing
    """
    for file_name in files:
        file_name = file_name[:-1]
        destination = os.path.join(destination, file_name)
        file = get_file_by_name(file_name, tree)
        file.copy(destination)


def add_file(file_path):
    """
    add_file creates new file at specified destination
    :param file_path: path of the new file
    :return: nothing
    """
    with open(file_path, 'w') as fp:
        pass
