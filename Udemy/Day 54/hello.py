from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''<h1>Hello World</h1>'''


@app.route('/hello')
def extra():
    return '''<h1>Hello World</h1>
              <p>You chose the hello endpoint</p> '''


if __name__ == "__main__":
    app.run()

