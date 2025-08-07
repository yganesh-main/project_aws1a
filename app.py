from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from GitHub Actions CI/CD!"

@app.route('/about')
def about():
    return "Deployed via GitHub Actions to EC2 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
