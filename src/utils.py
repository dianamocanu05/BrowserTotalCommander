import os


def create_html_list(index, root):
    """
    create_html_list creates the html code representing the list of children of given root
    it also edits the code so that various actions can take place (click, double click)
    :param index: 1 or 2(left or right panel)
    :param root: current root
    :return: html code
    """
    if root is not None:
        html_code = "<div><ul>\n"
        for c in root.children:
            html_code += "<li><img src='" + get_format_icon(c) + "'" + "style='width: 30px; height: 30px;'>"
            html_code += "<a id=" + "'" + c.name + str(index) + "' " + " oncontextmenu=\"highlight('" + c.name + str(
                index) + "');\" style='color:#000000" \
                         ";' ondblclick=\"expand('" + c.name + str(index) + "');\">" + \
                         get_printable_information(c) + "</a></li>\n"
        html_code += "</ul></div>"

        return html_code


def get_printable_information(file):
    """
    get_printable_information creates a string containing information about a file:
    name, extension, size, creation date, permissions mask
    :param file: file
    :return: information string
    """
    info = file.name + " - " + file.get_extension() + " - " + str(file.get_size()) + " - " + str(
        file.get_creation_date()) \
           + " - " + str(file.get_permissions_mask())
    return info


def get_format_icon(file):
    """
    get_format_icon returns the path to the icon representing the format of the given file
    :param file: file
    :return: path to icon
    """
    img_path = 'static/media/icons'
    if file.get_extension() is '':
        return os.path.join(img_path, 'folder.png')
    if file.get_extension() == '.png' or file.get_extension() == '.jpg':
        return os.path.join(img_path, 'image-file.png')
    if file.get_extension() == '.mp3':
        return os.path.join(img_path, 'audio-file.png')
    if file.get_extension() == '.py':
        return os.path.join(img_path, 'python-file.png')
    if file.get_extension() == '.xml':
        return os.path.join(img_path, 'xml-file.png')
    if file.get_extension() == '.mp4':
        return os.path.join(img_path, 'video-file.png')
    if file.get_extension() == '.txt':
        return os.path.join(img_path, 'text-file.png')
    if file.get_extension() == '.pdf':
        return os.path.join(img_path, 'pdf-file.png')
    if file.get_extension() == '.html':
        return os.path.join(img_path, 'html-file.png')
    if file.get_extension() == '.docx':
        return os.path.join(img_path, 'docx-file.png')
    return os.path.join(img_path, 'blank-file.png')


def get_file_by_name(name, tree):
    """
    get_file_by_name returns the file having the given name
    :param name: name
    :param tree: tree
    :return: file
    """
    for f in tree:
        if f.name == name:
            return f


def get_file_by_path(path, tree):
    """
    get_file_by_path returns the file having the given path
    :param path: path
    :param tree: tree
    :return: file
    """
    for f in tree:
        if f.path == path:
            return f


def get_file_by_name_ancestor(name, tree, ancestor):
    """
    get_file_by_name_ancestor returns the file having the given name and minimal distance between itself and given
    ancestor
    :param name: name
    :param tree: tree
    :param ancestor: ancestor
    :return: file
    """
    minim = 100
    desired_file = None
    for f in tree:
        if f.name == name and ancestor in f.get_ancestors():
            if f.get_ancestor_level(ancestor) < minim:
                minim = f.get_ancestor_level(ancestor)
                desired_file = f
    return desired_file
