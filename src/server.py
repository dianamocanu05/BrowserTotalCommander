from src.file_manager import get_file_tree
from src.utils import create_html_list, get_file_by_name
from flask import Flask, render_template, send_from_directory, request
from src.constants import constants

app = Flask(__name__, template_folder='templates', static_url_path='/static')
working_dir = constants['working_dir']
tree = get_file_tree(working_dir)
html_code1 = create_html_list(1, tree[0])
html_code2 = create_html_list(2, tree[0])


@app.route('/')
def home():
    global working_dir
    global tree

    # html_code1 = create_html_list(1, tree[0])
    # html_code2 = create_html_list(2, tree[0])
    return render_template('template.html', list={'list1': html_code1, 'list2': html_code2, 'working_dir': working_dir})


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
    return request.json


@app.route('/expand', methods=['POST'])
def expand():
    global html_code1, html_code2
    to_expand = request.json['expand']
    file = get_file_by_name(to_expand[:-1], tree)
    if to_expand[-1] == '1':
        html_code1 = create_html_list(1, file)
        return html_code1
    else:
        html_code2 = create_html_list(2, file)
        return html_code2


if __name__ == '__main__':
    app.run(debug=True)
