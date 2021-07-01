from flask import Flask
import os

app = Flask(__name__)
env_name = os.getenv("ENVIRONMENT_NAME", "default")

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
