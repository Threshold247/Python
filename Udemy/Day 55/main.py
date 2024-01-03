from flask import Flask

app = Flask(__name__)


# create bold decorator
def bold_decorator(function):
    def bold_wrapper():
        # call function and store in a variable called element
        element = function()
        # wrap the element in bold tag
        return f"<b>{element}<b/>"
    return bold_wrapper


# create underline decorator
def underline_decorator(function):
    def underline_wrapper():
        element = function()
        return f"<u>{element}<u/>"
    return underline_wrapper


def italic_decorator(function):
    def italic_wrapper():
        element = function()
        return f"<em>{element}<em/>"
    return italic_wrapper


# set up a normal route
@app.route("/")
@bold_decorator
@underline_decorator
@italic_decorator
def hello():
    # inline styling must ensure attribute is a string. eg <h2 style = "color: red">
    return f"<h2>Hello</h2>"


# set up a user route which takes an input of name
@app.route("/user/<name>")
# name is the argument
def greeting(name):
    return f"<h2>Hello {name}</h2>"


if __name__ == "__main__":
    app.run(debug=True)
