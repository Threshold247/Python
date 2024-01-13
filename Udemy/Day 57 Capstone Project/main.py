from flask import Flask, render_template
from post import Post

app = Flask(__name__)

blog_url = "https://api.npoint.io/bcdde3835375fdeab457"

blog_posts = Post(blog_url)


# create a route which displays only the Title and Subtitle of the blogs on the homepage. Passes the blog post object
# over to the index.html

@app.route('/')
def home():
    return render_template("index.html", blogs=blog_posts.list)


# create a route which only displays the Title and Body of the selected blog post. Passes the blog id over to the
# blog html file as well as the blog post object
@app.route('/blog/<int:blog_id>')
def get_blogs(blog_id):
    return render_template('post.html', blog_id=blog_id, blogs=blog_posts.list)


if __name__ == "__main__":
    app.run(debug=True)
