from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


# Main directory
UPLOAD_FOLDER = '/static'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['UPLOAD FOLDER'] = UPLOAD_FOLDER

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


# Create a user_loader callback. Connects to the User table
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
# New addition is the UserMixin
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


# register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user_email = request.form.get("email")
        user = db.session.execute(db.select(User).where(User.email == user_email)).scalar_one()
        if user:
            # User already exists
            flash("Email already exists", category="error")
            return redirect(url_for('register'))
        # hash and salt user password
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        # ignore the unexpected argument error
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        # Can redirect() and get name from the current_user
        return redirect(url_for("secrets", name=new_user.name))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        login_email = request.form.get('email')
        login_password = request.form.get('password')
        try:
            # find the user in the dbase and return an object
            user = db.session.execute(db.select(User).where(User.email == login_email)).scalar_one()
            if check_password_hash(user.password, login_password):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                print("Login unsuccessful")
                flash("Incorrect password", category="error")
                return redirect(url_for('login'))
        except Exception:
            flash("Email does not exist", category="error")
            return redirect(url_for('login'))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets/')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
