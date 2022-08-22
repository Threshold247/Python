################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    return enemies


increase_enemies()
print(f"enemies outside function: {enemies}")
print(enemies+increase_enemies())
