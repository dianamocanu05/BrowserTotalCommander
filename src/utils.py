

def create_html_list(tree, root):
    html_code = "<div><ul>"
    for c in root.children:
        html_code += "<li><a>" + get_printable_information(c) + "</a></li>"
    html_code += "</ul></div>"
    return html_code


def get_printable_information(file):
    info = file.name + " " + file.get_extension() + " " + str(file.get_size()) + " " + str(file.get_creation_date()) \
           + " " + str(file.get_permissions_mask())
    return info


