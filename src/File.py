import os


class File:

    def __init__(self, name, path, level, parent):
        self.name = name
        self.path = path
        self.level = level
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