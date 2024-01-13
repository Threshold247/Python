from datetime import datetime
from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_gender(name):
    params = {
        "name": name
    }
    my_request = requests.get(url="https://api.genderize.io", params=params)
    response = my_request.json()
    gender = response['gender']
    return gender


def get_age(name):
    params = {
        "name": name
    }
    my_request = requests.get(url="https://api.agify.io", params=params)
    response = my_request.json()
    age = response['age']
    return age


@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template("index.html", year=current_year)


@app.route('/guess/<name>')
def guess(name):
    # setup functions to take the name entered as a parameter in the url to get the gender and age
    gender = get_gender(name=name)
    age = get_age(name=name)
    return render_template("guess.html", name=name.capitalize(), gender=gender, age=age)


@app.route('/blog')
def blog_post():
    data = requests.get(url="https://api.npoint.io/bcdde3835375fdeab457")
    response = data.json()
    list = response['data']
    return render_template("blog.html", list=list)


if __name__ == '__main__':
    app.run(debug=True)
