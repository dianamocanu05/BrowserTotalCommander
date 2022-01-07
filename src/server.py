from src.file_manager import get_file_tree
from src.utils import create_html_list, get_file_by_name, get_file_by_name_ancestor
from src.actions import copy_paste, add_file
from flask import Flask, render_template, send_from_directory, request
from src.constants import constants
import os

app = Flask(__name__, template_folder='templates', static_url_path='/static')
working_dir1 = constants['working_dir']
working_dir2 = constants['working_dir']
tree = get_file_tree(working_dir1)
root1 = tree[0]
root2 = tree[0]
html_code1 = create_html_list(1, tree[0])
html_code2 = create_html_list(2, tree[0])
selected = []
to_copy = []
index = -1




@app.route('/')
def home():
    global working_dir1
    global tree

    return render_template('template.html',
                           list={'list1': html_code1, 'list2': html_code2, 'working_dir': working_dir1})


@app.route('/media/<path:path>')
def send_png(path):
    return send_from_directory('static/media', path)


@app.route('/style/<filename>')
def send_css(filename):
    return send_from_directory('static/style', filename)


@app.route('/editor.html')
def send_editor():
    file = get_file_by_name(selected[0][:-1], tree)
    return render_template('editor.html', text=file.read())


@app.route('/scripts/<filename>')
def send_py(filename):
    return send_from_directory('scripts', filename)


@app.route('/selected', methods=['POST'])
def addSelected():
    global selected
    selected = request.json["selected"]
    print(selected)
    return request.json


@app.route('/expand', methods=['POST'])
def expand():
    global html_code1, html_code2, working_dir1, working_dir2, root1, root2
    to_expand = request.json['expand']
    file = get_file_by_name(to_expand[:-1], tree)
    if to_expand[-1] == '1':
        working_dir1 = root1 = file
        html_code1 = create_html_list(1, file)
        return html_code1
    else:
        working_dir2 = root2 = file
        html_code2 = create_html_list(2, file)
        return html_code2


@app.route('/back', methods=['POST'])
def go_back():
    global html_code1, html_code2, working_dir1, working_dir2, root1, root2
    index = request.json['index']
    if str(index) == '1':
        html_code1 = create_html_list(1, root1.parent)
        working_dir1 = root1 = root1.parent
        if html_code1 is not None:
            return html_code1
    else:
        html_code2 = create_html_list(2, root2.parent)
        working_dir2 = root2 = root2.parent
        if html_code2 is not None:
            return html_code2
    return ""


@app.route('/copy', methods=['POST'])
def copy():
    global html_code1, html_code2, working_dir1, working_dir2, root1, root2, to_copy
    index = request.json['index']
    to_copy = selected
    return "success"


@app.route('/delete-file', methods=['POST'])
def delete_file():
    global tree, selected, html_code1, html_code2, root1, root2
    to_delete = selected
    index = request.json['index']

    for file_name in to_delete:
        file_name = file_name[:-1]
        if str(index) == '1':
            file = get_file_by_name_ancestor(file_name, tree, root1)
        else:
            file = get_file_by_name_ancestor(file_name, tree, root2)
        file.delete()

    tree = get_file_tree(constants['working_dir'])

    new_root1 = get_file_by_name(root1.name, tree)
    root1 = new_root1
    html_code1 = create_html_list(1, new_root1)

    new_root2 = get_file_by_name(root2.name, tree)
    root2 = new_root2
    html_code2 = create_html_list(2, new_root2)

    return {"html1": html_code1, "html2": html_code2}


@app.route('/paste', methods=['POST'])
def paste():
    global html_code1, html_code2, working_dir1, working_dir2, root1, root2, to_copy, tree

    index = request.json['index']
    if str(index) == '1':
        copy_paste(to_copy, root1.path, tree)
        tree = get_file_tree(constants['working_dir'])
        new_root1 = get_file_by_name(root1.name, tree)
        root1 = new_root1
        html_code1 = create_html_list(1, new_root1)
        return html_code1

    elif str(index) == '2':
        copy_paste(to_copy, root2.path, tree)
        tree = get_file_tree(constants['working_dir'])
        new_root2 = get_file_by_name(root2.name, tree)
        root2 = new_root2
        html_code2 = create_html_list(2, new_root2)
        return html_code2


@app.route('/cwd', methods=['POST'])
def cwd():
    start = constants['working_dir']
    index = request.json['index']
    if str(index) == '1':
        return os.path.join('\\', os.path.relpath(root1.path, start))
    else:
        return os.path.join('\\', os.path.relpath(root1.path, start))


@app.route('/refresh', methods=['POST'])
def refresh():
    global tree, html_code1, html_code2
    index = request.json['index']
    tree = get_file_tree(constants['working_dir'])
    if str(index) == '1':
        new_root1 = get_file_by_name(root1.name, tree)
        html_code1 = create_html_list(1, new_root1)
        return html_code1
    else:
        new_root2 = get_file_by_name(root2.name, tree)
        html_code2 = create_html_list(2, new_root2)
        return html_code2


@app.route('/add', methods=['POST'])
def add():
    global index
    index = request.json['index']
    return "ok"


@app.route('/new-file', methods=['POST'])
def add_new_file():
    global index, tree, html_code1, html_code2, root1, root2
    new_file = request.json["file"]
    add_file(os.path.join(root1.path, new_file))
    tree = get_file_tree(constants['working_dir'])

    new_root1 = get_file_by_name(root1.name, tree)
    root1 = new_root1
    html_code1 = create_html_list(1, new_root1)

    new_root2 = get_file_by_name(root2.name, tree)
    root2 = new_root2
    html_code2 = create_html_list(2, new_root2)

    return {"html1": html_code1, "html2": html_code2}


@app.route('/edit', methods=['POST'])
def edit():
    global tree, root1, root2, html_code1, html_code2
    text = request.json["text"]
    file = get_file_by_name(selected[0][:-1], tree)
    file.write(text)

    tree = get_file_tree(constants['working_dir'])

    new_root1 = get_file_by_name(root1.name, tree)
    root1 = new_root1
    html_code1 = create_html_list(1, new_root1)

    new_root2 = get_file_by_name(root2.name, tree)
    root2 = new_root2
    html_code2 = create_html_list(2, new_root2)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
