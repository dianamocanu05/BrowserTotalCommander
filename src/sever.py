from src.file_manager import get_file_tree
from src.utils import create_html_list
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates', static_url_path='/static')


@app.route('/')
def home():
    tree = get_file_tree("../root")
    html_code = create_html_list(tree, tree[0])
    return render_template('template.html', list={'list': html_code})


@app.route('/media/<path:path>')
def send_png(path):
    return send_from_directory('static/media', path)


@app.route('/style/<filename>')
def send_css(filename):
    return send_from_directory('static/style', filename)


if __name__ == '__main__':
    app.run(debug=True)
