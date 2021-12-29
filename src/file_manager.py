import os
from src.File import File

working_dir = "../root"
tree = []


def get_file_tree(directory):

    root_file = File(name=os.path.basename(directory), parent=None, path=directory,level=0)
    tree.append(root_file)
    old_root = root_file
    for root, dirs, files in os.walk(directory):
        new = root.replace(directory, '')
        level = new.count(os.sep)
        new_root = File(name=os.path.basename(new), parent=old_root, path = new, level = level)
        tree.append(new_root)
        indent = ' ' * 4 * level
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            file = File(name=os.path.basename(f), parent=new_root, path = os.path.join(directory, f), level = level)
            tree.append(file)
        old_root = new_root




get_file_tree(working_dir)


for t in tree:
    if(t.parent != None):
        print(t.name + " ---  "+ t.parent.name)
    else:
        print(t.name)
