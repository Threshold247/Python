alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(encode_text, shift_amount):
    my_list = list()
    for letter in encode_text:
        if letter != " ":
            print('''________________________''')
            print(f"orignal letter {letter}")
            index_check = alphabet.index(letter)
            print(f"index check {index_check}")
            shift_letter_index = index_check + shift_amount
            print(f"shifted letter index {shift_letter_index}")
            if shift_letter_index > 25:
                diff = shift_letter_index - 26
                print(f"shifted letter {alphabet[diff]}")
                my_list += alphabet[diff]
            else:
                print(f"shifted letter {alphabet[shift_letter_index]}")
                my_list += alphabet[shift_letter_index]
        else:
            my_list += " "

        print(f"{text}")
        print(f"{''.join(my_list)}")
    
def decrypt(decode_text, shift_amount):
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
    my_list = list()
    for letter in decode_text:
        if letter != " ":
            print(f"original letter {letter}")
            index_check = alphabet.index(letter)
            print(f"index check {index_check}")
            shift_letter_index = index_check - shift_amount
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

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == 'encode':
    encrypt(encode_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(decode_text=text, shift_amount=shift)