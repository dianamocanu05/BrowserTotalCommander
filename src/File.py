import os
import datetime
from shutil import copyfile, rmtree


class File:
    level = 0  # by default

    def __init__(self, name, path, parent):
        """
        constructor of a File object
        :param name: file name
        :param path: file path
        :param parent: file parent
        """
        self.name = name
        self.path = path
        self.parent = parent
        self.children = []

    def get_extension(self):
        """
        get_extension extracts the extension of the current instance
        :return: extension
        """
        _, file_extension = os.path.splitext(self.path)
        return file_extension

    def get_size(self):
        """
        get_size extracts the size of the current instance
        :return: size
        """
        return os.path.getsize(self.path)

    def is_dir(self):
        """
        is_dir checks if the current instance is a directory
        :return: boolean
        """
        return os.path.isdir(self.path)

    def delete(self):
        """
        delete deletes the current instance from the file structure
        :return: nothing
        """
        if os.path.isdir(self.path):
            rmtree(self.path)
        else:
            os.remove(self.path)

    def rename(self, new_name):
        """
        rename renames the current instance
        :param new_name: new name
        :return: nothing
        """
        os.rename(self.path, new_name)

    def set_parent(self, parent):
        """
        set_parent sets the directory containing the current instance
        :param parent: parent
        :return: nothing
        """
        self.parent = parent

    def add_child(self, child):
        """
        add_child adds child of current instance
        :param child:
        :return: nothing
        """
        self.children.append(child)

    def set_level(self, level):
        """
        set_level sets the level (relative to ./root, DFS-like) of the current instance
        :param level: level
        :return: nothing
        """
        self.level = level

    def get_creation_date(self):
        """
        get_creation_date retrieves the creation date of the current instance
        :return: creation date
        """
        return datetime.datetime.fromtimestamp(os.path.getctime(self.path))

    def get_permissions_mask(self):
        """
        get_permissions_mask retrieves the permissions associated with the current instance in octal form
        :return: permissions mask
        """
        return oct(os.stat(self.path).st_mode)

    def copy(self, destination):
        """
        copy copies current instance to destination
        :param destination: destination
        :return: nothing
        """
        copyfile(self.path, destination)

    def read(self):
        """
        read reads the text content of the current instance
        :return: text content
        """
        file = open(self.path, "r")
        return file.read()

    def write(self, text):
        """
        write writes new text content to current instance
        :param text: text content
        :return: nothing
        """
        file = open(self.path, "w")
        file.write(text)
        file.close()

    def move(self, new_path):
        """
        move moves current instance to new destination
        :param new_path: new path
        :return: nothing
        """
        os.rename(self.path, new_path)

    def get_ancestors(self):
        """
        get_ancestors retrieves the ancestors of the current instance until root is reached
        :return: ancestors
        """
        ancestors = []
        parent = self.parent
        while parent is not None:
            ancestors.append(parent)
            parent = parent.parent
        return ancestors

    def get_ancestor_level(self, ancestor):
        """
        get_ancestor_level returns the distance between current instance and one of it's ancestors
        :param ancestor:
        :return: level
        """
        ancestors = self.get_ancestors()
        return ancestors.index(ancestor)
