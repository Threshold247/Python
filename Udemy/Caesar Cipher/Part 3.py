alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(text, shift, direction):
    if direction == 'encode':
        def encrypt(encode_text, shift_amount):
            my_list = list()
            for letter in encode_text:
                if letter != " ":
                    index_check = alphabet.index(letter)
                    shift_letter_index = index_check + shift_amount
                    if shift_letter_index > 25:
                        diff = shift_letter_index - 26
                        my_list += alphabet[diff]
                    else:
                        my_list += alphabet[shift_letter_index]
                else:
                    my_list += " "
            print(f"{''.join(my_list)}")
        encrypt(encode_text=text, shift_amount=shift)
    elif direction == 'decode':
        def decrypt(decode_text, shift_amount):
            my_list = list()
            for letter in decode_text:
                if letter != " ":
                    index_check = alphabet.index(letter)
                    shift_letter_index = index_check - shift_amount
                    if shift_letter_index > 25:
                        diff = 25 - shift_letter_index
                        my_list += alphabet[diff]
                    else:
                        my_list += alphabet[shift_letter_index]
                else:
                    my_list += " "
            print(f"{''.join(my_list)}")
        decrypt(decode_text=text, shift_amount=shift)


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text=text, shift=shift, direction=direction)
