from flask import Flask, jsonify, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from dotenv import load_dotenv
import os
import random
load_dotenv(".env")
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


@app.route('/search')
def search():
    # get the request param value for loc
    location = request.args.get('loc')
    find_cafe = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    cafes = find_cafe.scalars().all()
    if cafes:
        # return cafes matching location
        return jsonify(cafes=[to_dict(cafe) for cafe in cafes])
    else:
        # return error message and status code
        return jsonify(error={"Not found": "Location not found"}), 404


# HTTP POST - Create Record
@app.route('/add', methods=['GET', 'POST'])
def add():
    # get the value of the key called name if a post request is sent
    # name = request.values.get('name')
    try:
        if request.method == 'POST':
            add_cafe = Cafe(
                id=request.form.get('id'),
                name=request.form.get('name'),
                map_url=request.form.get('map_url'),
                img_url=request.form.get('img_url'),
                location=request.form.get('location'),
                #  If the field is filled it is True, if empty it is False.
                has_sockets=bool(request.form.get("sockets")),
                has_toilet=bool(request.form.get("toilet")),
                has_wifi=bool(request.form.get("wifi")),
                can_take_calls=bool(request.form.get("calls")),
                seats=request.form.get("seats"),
                coffee_price=request.form.get("coffee_price"),
            )
            db.session.add(add_cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully added the cafe"}), 200
    except Exception as error:
        return jsonify({"error": {"message": str(error)}}), 500


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['GET', 'POST', 'PATCH'])
def update_price(cafe_id):
    try:
        # get value of request param
        new_price = request.values.get('new_price')
        # check if cafe exists by checking data for cafe id
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar_one()
        # if the data exist update the new price
        if cafe:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(f"success: {cafe_id} updated price to {new_price}"), 200
        else:
            return jsonify({"error": {"message": "Cafe id does not exist"}}), 500
    except Exception:
        return jsonify({"}error": {"message": "Cafe id does not exist or price was not inserted"}}), 500


# HTTP DELETE - Delete Record
@app.route('/review-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    try:
        api_key = request.args.get('api_key')
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar_one()
        # if api key matches whats on record, delete the cafe with the matching id.
        if api_key == os.getenv('api-key'):
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(f"success: {cafe_id} has been deleted"), 200
        else:
            return jsonify({"error": {"message": "api-key is incorrect"}}), 403
    except Exception:
        return jsonify({"error": {"message": "Cafe id does not exist"}}), 404


if __name__ == '__main__':
    app.run(debug=True)
