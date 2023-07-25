from email_validator import validate_email, EmailNotValidError
from sheety import DataManager

my_sheet = DataManager()
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


if email == email_check:
    print("You've joined the club")
    my_sheet.add_user(first=first_name, last=last_name, email=email)
else:
    print("email does not match")


