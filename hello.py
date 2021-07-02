from flask import Flask
import os
import os.path
from tkinter import *

app = Flask(__name__)
gui = Tk(className='Python Examples - Window Color')

@app.route("/")
def hello():
    gui.geometry("400x200")
    gui.configure(bg='blue')
    gui.mainloop()

    if os.path.isfile('/config/environment-name'):
        file1 = open("/config/environment-name", "r")
        env_name = file1.read()
    else:
        env_name = os.getenv("ENVIRONMENT_NAME", "default")

    return "Hello " + env_name + " Environment !!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
