
from Decryption import decrypt
from Encryption import encrypt


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


stop = False
while not stop:

    if direction == 'encode':
        encrypt(text, shift)
        stop = True
    elif direction == 'decode':
        decrypt(text, shift)
        stop = True
