from flask import Flask
import random
app = Flask(__name__)

number_list = []

for num in range(0, 10):
    number_list.append(num)

random_number = random.choice(number_list)

# home route
@app.route('/')
def home():
    return (f"<h2>Welcome to the guessing game<h2/>"
            f"<h1>Guess a number between 0 and 9<h1/>"
            f"<img/ src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


# guess route
@app.route('/<int:guess>')
def low(guess):
    if guess < random_number:
        return f"<h2 style='color:red' >Too low. Try again<h2/>"
    elif guess > random_number:
        return f"<h2 style='color:blue'>Too high. Try again<h2/>"
    else:
        return (f"<h2 style = 'color:green'>You win! You guessed correctly<h2/>"
                f"<p> The correct number is {random_number}<p/>")


if __name__ == "__main__":
    app.run(debug=True)
