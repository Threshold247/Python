import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {index: row for (index, row) in data.iterrows()}
test = {row.letter: row.code for row in nato_alphabet.values()}
print(test)


def generate_alphabet():
    # Create a list of the phonetic code words from a word that the user inputs.
    user_input = input("Enter a word:").upper()
    try:
        result = [test[letter] for letter in user_input]
    except KeyError:
        print("Please enter a letter")
    # re-run the function
        generate_alphabet()
    else:
        print(result)


generate_alphabet()


