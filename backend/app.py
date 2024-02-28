# will complete api requests in this folder for now

from flask import Flask
from openai import OpenAI

client = OpenAI()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'wassam'

if __name__ == '__main__':
    app.run(debug=True)