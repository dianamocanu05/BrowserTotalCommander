import os
import datetime
from shutil import copyfile, rmtree


class File:
    level = 0  # by default

    def __init__(self, name, path, parent):
        self.name = name
        self.path = path
        self.parent = parent
        self.children = []

    def get_extension(self):
        _, file_extension = os.path.splitext(self.path)
        return file_extension

    def get_size(self):
        return os.path.getsize(self.path)

    def is_dir(self):
        return os.path.isdir(self.path)

    def delete(self):
        if os.path.isdir(self.path):
            rmtree(self.path)
        else:
            os.remove(self.path)

    def rename(self, new_name):
        os.rename(self.path, new_name)

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def set_level(self, level):
        self.level = level

    def get_creation_date(self):
        return datetime.datetime.fromtimestamp(os.path.getctime(self.path))

    def get_permissions_mask(self):
        return oct(os.stat(self.path).st_mode)

    def copy(self, destination):
        copyfile(self.path, destination)

    def read(self):
        file = open(self.path, "r")
        return file.read()

    def write(self, text):
        file = open(self.path, "w")
        file.write(text)
        file.close()

    def get_ancestors(self):
        ancestors = []
        parent = self.parent
        while parent is not None:
            ancestors.append(parent)
            parent = parent.parent
        return ancestors

    def get_ancestor_level(self, ancestor):
        ancestors = self.get_ancestors()
        return ancestors.index(ancestor)