from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

current_year = datetime.now().year
print(current_year)


@app.route('/')
def home():

    return render_template('test.html', current_year=current_year)


if __name__ == '__main__':
    app.run(debug=True)
