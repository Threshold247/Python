fruits = ["Apple", "Pear", "Peach"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print(f"Fruit pie")
    else:
        print(fruit + " pie")


make_pie(1)
