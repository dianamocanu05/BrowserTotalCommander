import os
from src.File import File
from src.utils import get_printable_information
from src.constants import constants

working_dir = constants['working_dir']


def print_file_structure(file_tree, current):
    """
    print_file_structure prints the formatted file tree recursively
    :param file_tree: tree
    :param current: current root
    :return: nothing
    """
    for c in current.children:
        indent = "---" * c.level
        print(indent, c.name)
        print_file_structure(file_tree, c)


def get_file_by_path(files, path):
    """
    get_file_path returns the File object having the given path
    :param files: all files
    :param path: path
    :return: file
    """
    for f in files:
        if f.path == path:
            return f


def set_children(file_tree, file):
    """
    set_children sets the children of file by checking whose parent it is
    :param file_tree: tree
    :param file: file
    :return: nothing
    """
    for f in file_tree:
        if f.parent is file:
            file.add_child(f)


def compute_level(file):
    """
    compute_level computes the level of a file by iterating over it's ancestors
    :param file: file
    :return: level
    """
    level = 0
    parent = file.parent
    while parent is not None:
        level = level + 1
        parent = parent.parent
    return level


def get_file_tree(directory):
    """
    get_file_tree creates the file tree by exploring the directory and setting the corresponding child-parent
    relationships
    :param directory: directory
    :return: tree
    """
    file_tree = []
    file = File(os.path.basename(directory), os.path.abspath(directory), None)
    file_tree.append(file)
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            path = os.path.abspath(os.path.join(root, d))
            parent = get_file_by_path(file_tree, os.path.dirname(path))
            file = File(os.path.basename(path), path, parent)
            file_tree.append(file)
        for f in files:
            path = os.path.abspath(os.path.join(root, f))
            parent = get_file_by_path(file_tree, os.path.dirname(path))
            file = File(os.path.basename(path), path, parent)
            file_tree.append(file)

    for f in file_tree:
        set_children(file_tree, f)
        f.set_level(compute_level(f))

    return file_tree


if __name__ == "__main__":
    tree = get_file_tree(working_dir)
    for f in tree:
        print(get_printable_information(f))
