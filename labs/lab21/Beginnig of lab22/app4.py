from flask import Flask, render_template, request
from change.change import change

app = Flask(__name__, template_folder="templates",static_folder="static")

app.register_blueprint(change)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')



if __name__ == '__main__':
    app.run(debug=True)
