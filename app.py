from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

tpl_text = "My name is {{name}}. I love {{lang}} so much."

@app.route('/')
def hello():
    return "Hello"

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()