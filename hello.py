from flask import Flask
import os
import os.path
from flask import render_template
import socket
import random

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR') or random.choice(["red","green","blue","blue2","darkblue","pink"])

@app.route("/")
def hello():
    if os.path.isfile('/config/environment-name'):
        file1 = open("/config/environment-name", "r")
        env_name = file1.read()
    else:
        env_name = os.getenv("ENVIRONMENT_NAME", "default")

    print(color)
    contents = "Hello " + env_name + " Environment !!"
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[new_color])

@app.route('/read-file')
def read_file():
    if os.path.isfile('/config/environment-name'):
        f = open("/config/environment-name")
        contents = f.read()
    else:
        contents = "File not found"

    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
