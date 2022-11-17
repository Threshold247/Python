# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Letters/starting_letter.txt') as file:
    starting_letter = file.read()

with open('./Input/Names/invited_names.txt') as file:
    # created a list of names
    invited_names = file.readlines()
    # loop through the list to get each name
    for name in invited_names:
        # strip away any white space
        strip_name = name.strip()
        # replace the name with the new name from invited name list
        new_letter = starting_letter.replace('[name]', strip_name)
        print(new_letter)
        # write each name to a text file of the same name
        with open(f'./Output/ReadyToSend/letter_for_{strip_name}.txt', mode="w") as file1:
            file1.write(new_letter)
