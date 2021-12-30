from src.file_manager import get_file_tree
from src.utils import create_html_list
from flask import Flask, render_template, send_from_directory
from src.constants import constants

app = Flask(__name__, template_folder='templates', static_url_path='/static')

working_dir = constants['working_dir']


@app.route('/')
def home():
    tree = get_file_tree(working_dir)
    html_code = create_html_list(tree, tree[0])
    return render_template('template.html', list={'list': html_code, 'working_dir': working_dir})


@app.route('/media/<path:path>')
def send_png(path):
    return send_from_directory('static/media', path)


@app.route('/style/<filename>')
def send_css(filename):
    return send_from_directory('static/style', filename)


@app.route('/scripts/<filename>')
def send_py(filename):
    return send_from_directory('scripts', filename)


if __name__ == '__main__':
    app.run(debug=True)
