#  Write a Python script to check whether a given key already exists in a dictionary


def check(key, dict):
    return key in dict


mydict = {1: "one", 2: "two"}
print(check(1, mydict))
print(check(3, mydict))
