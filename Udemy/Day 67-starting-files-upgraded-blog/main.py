import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for,request,jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

load_dotenv('.env')

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['CKEDITOR_PKG_TYPE'] = 'full'
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = os.getenv('api-key')
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# Create form

class MyForm(FlaskForm):
    # adding a validators requires a valid input which will prompt user to fill out the input.
    title = StringField(label='Title', validators=[DataRequired()])
    subtitle = StringField(label='Subtitle', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    img_url = StringField(label='Image URL', validators=[URL()])
    # requires CKEditor because of the amount of text required
    body = CKEditorField(label='Blogpost Body', validators=[DataRequired()])
    submit_btn = SubmitField(label="Submit blog")


@app.route('/')
def get_all_posts():
    # Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.date)).scalars().all()
    return render_template("index.html", all_posts=posts)


# Add a route so that you can click on individual posts.
@app.route('/single/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# add_new_post() to create a new blog post
@app.route('/new_post/', methods=['GET', 'POST', 'PATCH'])
def add_new_post():
    form = MyForm()
    if form.validate_on_submit():
        try:
            add_post = BlogPost(
                    title=request.form.get("title"),
                    subtitle=request.form.get("subtitle"),
                    date=date.today().strftime('%B %d,%Y'),
                    body=request.form.get('body'),
                    author=request.form.get("author"),
                    img_url=request.form.get("img_url")
                )
            db.session.add(add_post)
            db.session.commit()
            return redirect(url_for('get_all_posts'))
        except Exception as error:
            return jsonify({"error": {"message": str(error)}}), 500
    return render_template('make-post.html', form=form)


# edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>')
def edit_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    edit_form = MyForm(
        title=requested_post.title,
        subtitle=requested_post.subtitle,
        date=requested_post.date,
        body=requested_post.body,
        author=requested_post.author,
        img_url=requested_post.img_url
    )
    return render_template('make-post.html', form=edit_form, post_id=post_id)


# delete_post() to remove a blog post from the database
@app.route('/delete-post/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        api_key = request.args.get('api-key')
        blog_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar_one()
        # check if the api key matches the one on record.
        if api_key == os.getenv('api-key'):
            db.session.delete(blog_to_delete)
            db.session.commit()
    except Exception as error:
        print(error)


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
