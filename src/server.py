from src.file_manager import get_file_tree
from src.utils import create_html_list, get_file_by_name
from src.actions import copy_paste
from flask import Flask, render_template, send_from_directory, request
from src.constants import constants

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


@app.route('/')
def home():
    global working_dir1
    global tree

    # html_code1 = create_html_list(1, tree[0])
    # html_code2 = create_html_list(2, tree[0])
    return render_template('template.html',
                           list={'list1': html_code1, 'list2': html_code2, 'working_dir': working_dir1})


@app.route('/media/<path:path>')
def send_png(path):
    return send_from_directory('static/media', path)


@app.route('/style/<filename>')
def send_css(filename):
    return send_from_directory('static/style', filename)


@app.route('/scripts/<filename>')
def send_py(filename):
    return send_from_directory('scripts', filename)


@app.route('/selected', methods=['POST'])
def addSelected():
    global selected
    selected = request.json["selected"]
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
    print(to_copy)
    return "success"


@app.route('/delete', methods=['POST'])
def delete():
    global tree, selected
    to_delete = selected
    for file_name in to_delete:
        file = get_file_by_name(file_name, tree)
        file.delete()
    tree = get_file_tree(constants['working_dir'])


@app.route('/paste', methods=['POST'])
def paste():
    global html_code1, html_code2, working_dir1, working_dir2, root1, root2, to_copy, tree
    index = request.json['index']
    if str(index) == '1':
        copy_paste(to_copy, root1.path, tree)
        tree = get_file_tree(constants['working_dir'])
        html_code1 = create_html_list(1, root1)
        return html_code1

    else:
        copy_paste(to_copy, root2.path, tree)
        tree = get_file_tree(constants['working_dir'])
        html_code2 = create_html_list(2, root2)
        return html_code2


@app.route('/cwd', methods=['POST'])
def cwd():
    index = request.json['index']
    if str(index) == '1':
        return root1.path
    else:
        return root2.path


if __name__ == '__main__':
    app.run(debug=True)
