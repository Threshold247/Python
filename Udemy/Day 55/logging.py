inputs = eval(input())
# TODO : Create the logging decorator function


def logging_decorator(function):
    def wrapper(*args):
        # prints out the function name and arguments
        print(f"You accessed {function.__name__}{args}")
        # stores the result of the function in a variable called total. function takes multiple arguments and returns
        # a total
        result = function(*args)
        print(result)
    return wrapper


# TODO : Use the login decorator function

@logging_decorator
def a_function(a, b, c):
    return a*b*c


a_function(inputs[0], inputs[1], inputs[2])

