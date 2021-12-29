from django.shortcuts import render
from django import template
from src.file_manager import get_file_tree
from src.utils import create_html_list

linker = template.Library()


@linker.assignment_tag
def hello(request):
    tree = get_file_tree("../root")
    html_code = create_html_list(tree, tree[0])
    return render(request, 'template.html', {'list': html_code})
