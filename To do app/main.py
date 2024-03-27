from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
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


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    # add SQL here to get data from database
    # text input box for description
    # text input box for date
    # reminder button to highlight task
    # list all tasks on database
    task_list = db.session.execute(db.select(Task)).scalars()

    if request.method == "POST":
        check_reminder = request.form.get("reminder")
        if check_reminder == 'on':
            check_reminder = True
        else:
            check_reminder = False
        add_task = Task(
            description=request.form.get("description"),
            date=request.form.get("date"),
            reminder=check_reminder
        )
        db.session.add(add_task)
        db.session.commit()
    return render_template('tasks.html', tasks=task_list)


@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST', 'PATCH'])
def edit_task(task_id):
    task_to_edit = db.session.execute(db.select(Task).where(Task.id == task_id)).scalar_one()
    if request.method == 'POST':
        task_description = request.form.get("description")
        task_date = request.form.get("date")
        task_reminder = request.form.get("reminder")
        if task_description == "":
            unedited_description = task_to_edit.description
            print(unedited_description)
        else:
            edit_description = task_description
            print(edit_description)



        return redirect(url_for('tasks'))
    return render_template('edit.html', task=task_to_edit)


@app.route('/delete/<int:task_id>', methods=['GET', 'POST', 'DELETE'])
def delete_task(task_id):
    print(task_id)
    try:
        task_to_delete = db.session.execute(db.select(Task).where(Task.id == task_id)).scalar_one()
        db.session.delete(task_to_delete)
        db.session.commit()
    except Exception:
        print("error")
    return redirect(url_for('tasks'))


@app.route('/logout')
def logout():
    pass


if __name__ == "__main__":
    app.run(debug=True, port=5003)

