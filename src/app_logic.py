from src.file_manager import get_file_tree
from src.utils import create_html_list
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello():
    tree = get_file_tree("../root")
    html_code = create_html_list(tree, tree[0])
    return render_template('template.html', subprocess_output={'list': html_code})


if __name__ == '__main__':
    app.run(debug=True)
