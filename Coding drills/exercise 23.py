#  Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2

def sub_str(string, n):
    flen = 2
    if flen > len(string):
        flen = len(string)
    substr = string[:flen]
    print(substr)

    result = ""
    for i in range(n):
        result = result + substr
    return(result)


print(sub_str('abcdef', 2))
print(sub_str('p', 3))
