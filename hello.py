from flask import Flask
import os
import os.path

app = Flask(__name__)

@app.route("/")
def hello():
    if os.path.isfile('/config/environment-name'):
        file1 = open("/config/environment-name", "r")
        env_name = file1.read()
    else:
        env_name = os.getenv("ENVIRONMENT_NAME", "default")

    return "Hello " + env_name + " Environment !!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
