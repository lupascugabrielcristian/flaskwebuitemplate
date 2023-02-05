#main.py

from flask import Flask, request  
from flask import render_template
from flaskwebgui import FlaskUI # import FlaskUI
import random

app = Flask(__name__)
ui = FlaskUI(app=app, server="flask", width=500, height=500, port=5400) # add app and parameters



@app.route("/")
def hello():  
    def get_random_numbers():
        context['a'] = random.randrange(1, 100)
        context['b'] = random.randrange(100,200)

    context = {}
    context['name'] = "Cristi"
    context['a'] = 0
    context['b'] = 0
    context['get_numbers'] = get_random_numbers 
    return render_template('index.html', post=context)

@app.route("/some_page", methods=['GET'])
def home(): 
    args = request.args
    a = args['unu']
    b = args['doi']
    data = { 'val1': a, 'val2': b }
    return render_template('some_page.html', data=data)

@app.route("/keeponline", methods=['GET'])
def kepp_online():
    return "ok"

if __name__ == "__main__":
    # app.run() for debug
    ui.run()
