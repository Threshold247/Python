from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


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
class MyIndexForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    year = StringField(label='Year', validators=[DataRequired()])
    description = StringField(label='Description', validators=[DataRequired()])
    rating = StringField(label='Rating', validators=[DataRequired()])
    ranking = StringField(label='Ranking', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    img_url = StringField(label='Image URL', validators=[DataRequired(), URL()])
    submit_btn = SubmitField(label="Add movie")


class MyEditForm(FlaskForm):
    rating = StringField(label="Your rating out of 10 e.g 7.5 ", validators=[DataRequired()])
    review = StringField(label="Your review here", validators=[DataRequired()])
    done_btn = SubmitField(label="Done")


@app.route("/")
def home():
    # return movie data to home screen based on ranking.
    movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars()
    return render_template("index.html", movies=movies)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = MyIndexForm()
    form.validate_on_submit()

    # use this code block to send data to the db.
    if request.method == 'POST':
        print("It posted")
        print(f"{form.title.data}")
        add_movie = Movie(title=form.title.data, year=form.year.data, description=form.description.data,
                          rating=form.rating.data, ranking=form.ranking.data, review=form.review.data,
                          img_url=form.img_url.data)
        db.session.add(add_movie)
        # commit data to the table
        db.session.commit()
        # redirect to home screen after data is committed
        return redirect(url_for('home'))
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






@app.route("/select")
def select():
    return render_template("select.html")


if __name__ == '__main__':
    app.run(debug=True)
