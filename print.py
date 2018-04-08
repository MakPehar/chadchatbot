from main import *
from flask import Flask, render_template

msg = Chad()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html", msg=msg)

@app.route('/index.html')
def index():
    return render_template("index.html", msg=msg)
@app.route('/about.html')
def about():
    return render_template("about.html")
@app.route('/chat.html')

def chat():
    return render_template("chat.html")
if __name__ == "__main__":
    app.run()