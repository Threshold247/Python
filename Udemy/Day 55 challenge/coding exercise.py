from flask import Flask
import random


number_list = []

for num in range(0, 11):
    number_list.append(num)

random_number = random.choice(number_list)

app = Flask(__name__)


@app.route('/')
def home():
    return '''<h2>Welcome to the guessing game<h2/>
            <form>
                <div>
                    <label for="example">Enter a number</label>
                    <input id="example" type="text" name="text" />
                </div>
                <div>
                    <input type="submit" value="Send" />
                </div>
            </form>'''


@app.route('/low')
def low():
    return f"<h2>Too low. Try again<h2/>"


@app.route('/high')
def high():
    return f"<h2>Too high. Try again<h2/>"


@app.route('/correct')
def correct():
    return f"<h2>You win! You guessed correctly<h2/>"

# Checking user input against random number. redirect to high or low or correct route
# while not_correct:
#     if user_input < random_number:
#         print(f"Number is lower than the random number")
#         user_input = int(input("Enter a number: "))
#     elif user_input > random_number:
#         print(f"Number is higher than the random number")
#         user_input = int(input("Enter a number: "))
#     else:
#         print("You guessed correctly")
#         not_correct = False


if __name__ == "__main__":
    app.run(debug=True)


