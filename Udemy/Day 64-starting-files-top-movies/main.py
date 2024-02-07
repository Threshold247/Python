from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv
load_dotenv('.env')

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
movie_database_key = os.getenv('movie_database_key')
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# with app.app_context():
#     db.create_all()

# After adding the new_movie the code needs to be commented out/deleted.
# So you are not trying to add the same movie twice. The db will reject non-unique movie titles.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's
#     sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller
#     leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

# setup Flask form class with labels and validation
class MyAddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])

    submit_btn = SubmitField(label="Add movie")


class MyEditForm(FlaskForm):
    rating = StringField(label="Your rating out of 10 e.g 7.5 ", validators=[DataRequired()])
    review = StringField(label="Your review here", validators=[DataRequired()])
    done_btn = SubmitField(label="Done")


class MySelectForm(FlaskForm):
    pass


@app.route("/")
def home():
    # return movie data to home screen based on ranking.
    movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars()
    return render_template("index.html", movies=movies)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = MyAddForm()
    form.validate_on_submit()

    # use this code block to send data to the db.
    if request.method == 'POST':
        # connect to the movie database api, bring back the information.
        url = f"https://api.themoviedb.org/3/search/movie?query={form.title.data}&include_adult=false&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": os.getenv("Authorization")
        }

        response = requests.get(url, headers=headers)
        data = response.json()['results']

        return render_template('select.html', movies=data)
    return render_template("add.html", form=form)


@app.route("/edit/<movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar_one()
    form = MyEditForm()
    form.validate_on_submit()
    if request.method == "POST":
        # amend the rating
        movie.rating = float(form.rating.data)
        # amend the review
        movie.review = form.review.data
        # commit the changes
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html",  movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("movie_id")
    # movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar_one()
    # simpler format to get the selected movie from the database. Takes name of the table and the selector
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/select/<movie_id>", methods=['GET', 'POST'])
def select(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNTBmZDA3YmNhY2FhMzRiMDg2YjZkNGFmODQ2MDAxZSIsInN1YiI6IjY1YzFmYmZiYTA2NjQ1MDE2MTVkZmM2MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.0FviLyvHRIe36bZbKeMsfOd91y4KR5QViflSTWRaniM"
    }
    response = requests.get(url, headers=headers)
    movie = response.json()
    new_movie = Movie(
        title=movie['original_title'],
        img_url=f"{MOVIE_DB_IMAGE_URL}{movie['poster_path']}",
        year=movie['release_date'].split("-")[0],
        description=movie['overview']
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
