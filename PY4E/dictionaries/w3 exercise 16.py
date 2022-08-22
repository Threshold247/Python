# Write a Python program to get a dictionary from an object's fields


class dictObj ():
    def __init__(self):
        self.a = 'one'
        self.b = 'two'
        self.c = 'three'

    def doNothing(self):
        pass


test = dictObj()
print(test.__dict__)
