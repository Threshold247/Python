from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # get the value from key called name
    name = request.form['name']
    # get the value from key called password
    password = request.form.get('password')
    return f" <h1> Name:{name} and Password:{password} submitted</h1>"


if __name__ == '__main__':
    app.run(debug=True)
