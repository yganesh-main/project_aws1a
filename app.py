
from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.datetime.now()
    return f"<h1>Hello from EC2! 🚀</h1><p>Deployed at: {now}</p>"

@app.route("/about")
def about():
    return "This is a minimal Flask app deployed on EC2 without CodeDeploy or CodeBuild."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
