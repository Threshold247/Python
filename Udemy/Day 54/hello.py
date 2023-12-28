from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return f"<h1>Hello World</h1>"


@app.route('/hello')
def extra():
    return (f"<h1>Hello World</h1>"
            f"<p>Hello endpoint</p>")


if __name__ == "__main__":
    app.run()

