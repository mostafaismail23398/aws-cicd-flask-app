from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "CI/CD to AWS EC2 is Working 🚀"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)