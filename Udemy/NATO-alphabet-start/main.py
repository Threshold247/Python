import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {index: row for (index, row) in data.iterrows()}
test = {row.letter: row.code for row in nato_alphabet.values()}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word:").upper()

result = [test[letter] for letter in user_input]
print(result)


