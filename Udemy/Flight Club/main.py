from email_validator import validate_email, EmailNotValidError
import re


print("Welcome to Flight Club!")
print("We find the best flight prices for you")
first_name = input("Please add your first name: ")
last_name = input("Please add your last name: ")
email = input("Please add your email address: ")
try:
    email_valid = validate_email(email)
    print(email_valid)
except EmailNotValidError as e:
    print(str(e))
    email = input("Please add your email address: ")
email_check = input("Please type your email again: ")


def match_email(email1, email2):
    if email1 == email2:
        print("email matches")
    else:
        print("email does not match")


print(match_email(email1=email, email2=email_check))


