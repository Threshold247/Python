import os
from flask import Flask, render_template,request
import requests
import smtplib
import dotenv

dotenv.load_dotenv('.env')

USER_EMAIL = os.getenv('my_email')
USER_PASSWORD = os.getenv('my_password')
print(USER_EMAIL, USER_PASSWORD)
app = Flask(__name__)

blog_url = "https://api.npoint.io/bcdde3835375fdeab457"

blog_posts = requests.get(url=blog_url)
response = blog_posts.json()
blog_data = response['data']


def send_email(name, email, phone, message):
    # setup connection
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # set-up message sent from sender
        email_msg = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
        # enable encryption
        connection.starttls()
        # login
        connection.login(USER_EMAIL, USER_PASSWORD)
        # sending email from sender to recipient with message
        connection.sendmail(USER_EMAIL, USER_EMAIL, email_msg)


@app.route('/')
def home():
    return render_template('index.html', blog_data=blog_data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<blog_id>')
def blog(blog_id):
    print(blog_id)
    print(type(blog_id))
    return render_template('post.html', blog_data=blog_data, blog_id=int(blog_id))


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name, email, phone, message)
        return render_template('contact.html', method=request.method)

    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
