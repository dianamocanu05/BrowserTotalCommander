import os


def create_html_list(index, root):
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
    info = file.name + " - " + file.get_extension() + " - " + str(file.get_size()) + " - " + str(
        file.get_creation_date()) \
           + " - " + str(file.get_permissions_mask())
    return info


def get_format_icon(file):
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
    for f in tree:
        if f.name == name:
            return f


def get_file_by_path(path, tree):
    for f in tree:
        if f.path == path:
            return f


def get_file_by_name_ancestor(name, tree, ancestor):
    minim = 100
    desired_file = None
    for f in tree:
        if f.name == name and ancestor in f.get_ancestors():
            if f.get_ancestor_level(ancestor) < minim:
                minim = f.get_ancestor_level(ancestor)
                desired_file = f
    return desired_file
