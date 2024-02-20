import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
# # create a table with keys
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, "
# #                "author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

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

# # insert data

# with app.app_context():
#     # add data using class
#     book = Books(id=1, title='Harry Potter', author="J. K. Rowling", rating=9.3)
#     db.session.add(book)
#     # commit data to the table
#     db.session.commit()

# query data
with app.app_context():

# read data, returns an object
    result = db.session.execute(db.select(Books).order_by(Books.title)).scalars()
    for row in result:
        print(row.title)
        print(row.author)
        print(row.rating)





