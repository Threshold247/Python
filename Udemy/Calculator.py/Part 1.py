from art import logo

# Calculator
print(logo)


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return round(n1/n2, 2)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = int(input("What is the first number? "))
    should_calculate = True
    while should_calculate:
        my_list = []

        for item in operations:
            my_list += item

        my_operator = input(f"Select an operation {my_list}  ")
        num2 = int(input("What is the next number? "))

        function = operations[my_operator]
        output = function(n1=num1, n2=num2)
        print(f" {num1}{my_operator}{num2}={output}")

        question = input(
            "Select Y to continue calculating or N to start again or quit to exit program\n").lower()
        if question == 'y':
            num1 = output
        elif question == 'n':
            should_calculate = False
            print("Restarting calculator")
            calculator()
        else:
            should_calculate = False
            print("Program exited")


calculator()
