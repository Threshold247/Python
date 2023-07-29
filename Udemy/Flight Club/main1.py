from email_validator import validate_email, EmailNotValidError
from sheety import SheetManager

my_sheet = SheetManager()
print("Welcome to Flight Club!")
print("We find the best flight prices for you")
first_name = input("Please add your first name: ").title()
last_name = input("Please add your last name: ").title()

email = "email"
email2 = "email2"

while email != email2:
    email = input("Please add your email: ")
    if email == "exit" or email == "quit":
        exit()
    try:
        valid_email = validate_email(email)
    except EmailNotValidError as e:
        print(str(e))
        exit()
    email2 = input("Please verify your email : ")
    if email2.lower() == "quit" or email2.lower() == "exit":
        exit()
    break
print("You've joined the club")
my_sheet.add_user(first=first_name, last=last_name, email=email)





