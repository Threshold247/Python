alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def decrypt(text, shift):

    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"
    my_list = list()
    for letter in text:
        if letter != " ":
            print(f"original letter {letter}")
            index_check = alphabet.index(letter)
            print(f"index check {index_check}")
            shift_letter_index = index_check - shift
            print(f"shifted letter index {shift_letter_index}")
            if shift_letter_index > 25:
                diff = 25 - shift_letter_index
                print(f"shifted letter {alphabet[diff]}")
                my_list += alphabet[diff]
            else:
                print(f"shifted letter {alphabet[shift_letter_index]}")
                my_list += alphabet[shift_letter_index]
        else:
            my_list += " "
        print(f"{text}")
        print(f"{''.join(my_list)}")

    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
decrypt(text, shift)
