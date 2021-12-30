import os


def create_html_list(tree, root):
    html_code = "<div><ul>\n"
    for c in root.children:
        html_code += "<li><img src='" + get_format_icon(c) + "'" + "style='width: 30px; height: 30px;'>"
        html_code += "<a id=" + "'" + c.name + "' " + " onclick=\"highlight('" + c.name + "');\" style='color:#000000" \
                                                                                          ";'>" + \
                     get_printable_information(c) + "</a></li>\n"
    html_code += "</ul></div>"
    print(html_code)
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
    return os.path.join(img_path, 'blank-file.png')
