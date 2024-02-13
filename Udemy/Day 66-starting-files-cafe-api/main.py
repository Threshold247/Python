from flask import Flask, jsonify, render_template, request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

# Create Database once
# with app.app_context():
#     db.create_all()


def to_dict(self):
    #
    dictionary = {}
    # loop
    for column in self.__table__.columns:
        dictionary[column.name] = getattr(self, column.name)
    return dictionary


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET', 'POST'])
def random_cafe():
    # return all cafes
    result = db.session.execute(db.select(Cafe))
    # generate a random id by setting a range between 0 and maximum length
    cafe_id = random.randint(0, (len(result.all())))
    # return one random cafe
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar_one()
    return jsonify(cafe=to_dict(cafe))


@app.route("/all")
def all_cafes():
    # return all cafes in a list
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    # return each cafe in the list as a dictionary
    return jsonify(cafes=[to_dict(cafe) for cafe in cafes])


# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
