import random


#ref  = [1/ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]


def deal_card():
    """Deals a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_of_cards):
    """Takes a list of cards and returns the sum of the cards"""
    # Hint 7
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    # Hint 8
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    return sum(list_of_cards)


def compare(user_total, com_total):
    if user_total == com_total:
        return("Draw")
    elif user_total == 0:
        return("Player wins, black jack")
    elif com_total == 0:
        return("Dealer wins, black jack")
    elif user_total > 21:
        return ("Player has more than 21. You lose")
    elif com_total > 21:
        return ("Dealer has more than 21. You win")
    elif user_total > com_total:
        return("Player wins")
    else:
        return "You lose"


user_cards = []
computer_cards = []
gameOver = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
# print(user_cards)
# print(computer_cards)

# Hint 11

while not gameOver:
    # Hint 9
    user_total = (calculate_score(user_cards))
    com_total = (calculate_score(computer_cards))

    print(f"User cards are: {user_cards},current score: {user_total}")
    print(f"Deal cards are: {computer_cards[0]}")
    # Hint 10
    if user_total == 0 or com_total == 0 or user_total > 21:
        # if
        gameOver = True

    else:
        user_wants_to_hit = input(
            "Type Yes to get another card or No to stay: ").lower()
        if user_wants_to_hit == 'yes':
            user_cards.append(deal_card())
            print(user_cards, computer_cards)
        else:
            gameOver = True
while com_total != 0 and com_total < 17:
    computer_cards.append(deal_card())
    com_total = sum(computer_cards)

print(compare(user_total, com_total))
print(f"User cards are: {user_cards}, final score: {user_total}")
print(f"computer_cards are: {computer_cards}, final score: {com_total}")
