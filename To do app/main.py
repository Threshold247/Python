from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
from dotenv import load_dotenv

load_dotenv(".env")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
# New addition is the UserMixin
class Task(db.Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String(100))
    date: Mapped[str] = mapped_column(String(100))
    reminder: Mapped[bool] = mapped_column()


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/tasks')
def tasks():
    # add SQL here to get data from database
    # text input box for description
    # text input box for date
    # reminder button to highlight task
    # list all tasks on database
    return render_template('tasks.html')


@app.route('/logout')
def logout():
    pass


if __name__ == "__main__":
    app.run(debug=True, port=5003)

