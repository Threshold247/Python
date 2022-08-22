# Write a Python program to test whether a passed letter is a vowel or not

def test(letter):
    if letter.lower() in 'aeiou':
        print("This is a vowel")
    else:
        print("This is a constant")


test("A")
test("b")
