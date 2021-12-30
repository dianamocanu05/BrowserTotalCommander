from src.server import app




def delete():
    print('Delete')


def move_rename():
    print('Move/Rename')


def add():
    print('Add')


def edit():
    print('Edit!')


@app.route('/select')
def select():
    print("Select")
