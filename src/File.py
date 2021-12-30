import os
import datetime


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
