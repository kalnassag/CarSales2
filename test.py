from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1 style=""color:red""> Hello, World!</h1>"


@app.route("/secret")
@app.route("/secret2")
def secret():
    return "<h1 style=""color:yello""> You found the secret!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
