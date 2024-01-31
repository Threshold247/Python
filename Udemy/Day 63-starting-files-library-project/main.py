from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


# CREATE TABLE
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # select query to db returns an object which can be looped through (done in the index.html)
    all_books = db.session.execute(db.select(Books).order_by(Books.title)).scalars()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        # add a new book using table schema
        book = Books(title=request.form.get('title'), author=request.form.get('author')
                     , rating=request.form.get('rating'))
        db.session.add(book)
        # commit data to the table
        db.session.commit()
        # redirect to home screen after data is committed
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    if request.method == 'POST':
        # grab the rating from the input
        rating = request.form['rating']
        # select the book associated with book id
        change_rating = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar_one()
        # add the new rating which was taken from above
        change_rating.rating = rating
        # commit changes to the database.
        db.session.commit()
        # redirect after the changes are committed to the dbase
        return redirect(url_for('home'))
    # select a specific book associated with book id
    selected_book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar_one()
    return render_template('edit.html', book=selected_book)


@app.route("/delete")
def delete():
    book_id = request.args.get('book_id')
    # DELETE A RECORD BY ID
    # Alternative way to select the book to delete.
    # book_to_delete = db.get_or_404(Books, book_id)

    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

