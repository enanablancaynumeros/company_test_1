import os

from flask import Flask
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def roman_calculator():
    return "Hello World!"


if __name__ == "__main__":
    port = os.environ["API_PORT"]
    app.run(host="localhost", port=port)
