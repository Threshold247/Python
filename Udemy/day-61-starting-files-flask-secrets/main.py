from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

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
app.secret_key = "1234"


# create class and set attributes
class MyForm(FlaskForm):
    # adding a validators requires a valid email input which will prompt user to fill out the input.
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    # adding a validator which requires an input and a minimum length of 8 characters
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit_btn = SubmitField(label="Submit")


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # access the class storing it in a variable. pass the variable attributes and methods over to the login.html
    form = MyForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        print(request.form['email'])
        print(request.form['password'])
        return redirect()
    return render_template('login.html', form=form)


@app.route('/success')
def redirect():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
