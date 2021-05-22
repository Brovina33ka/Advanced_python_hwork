from flask import Flask, render_template, request, Blueprint
from db11 import JsonDatabase



database = JsonDatabase(
    '/Users/Ksenia/Desktop/cmder/Workspace/lab21/HW/change/data/db.txt'
)

database.save('Как РТ, только БМ БМ БМ!!!!!')

blueprint = Blueprint(
    name='change',
    import_name=__name__,
    template_folder='templates'

)


change = Blueprint('change', __name__, template_folder='templates', static_folder='static')



@change.route('/', methods=("GET", "POST"))
def Change_stroke():
    if request.method == 'GET':
        return render_template('index.html')

    database.save(
        text=request.form['text']
        
    )
    if request.method == 'PUT':
        text = database.get()
        return render_template('index.html')

