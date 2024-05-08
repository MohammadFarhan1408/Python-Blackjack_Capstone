import random
from art import artwork
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(card_list):
    return sum(card_list)


def update_ace(card_list):
    if 11 in card_list and calculate_score(card_list) > 21:
        ace_index = card_list.index(11)
        card_list[ace_index] = 1


user_cards = random.choices(cards, k=2)
computer_cards = random.choices(cards, k=2)


# Check if ace needs to be reduced to 1
update_ace(user_cards)
update_ace(computer_cards)

# Print initial hands
print(artwork)
print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
print(f"Computer's cards: [{computer_cards[0]}, #]")

# Check for immediate blackjack
if calculate_score(user_cards) == 21:
    print("BlackJack, You Win")
    exit()
elif calculate_score(computer_cards) == 21:
    print("BlackJack, You Loose")
    print(f"Computer's cards: {computer_cards}")
    exit()

user_resume = True
# Player's turn
while user_resume:
    user_action = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if user_action == 'y':
        user_cards += random.choices(cards, k=1)
        update_ace(user_cards)
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        if user_score > 21:
            print("Busted! You Lose")
            exit()
    elif user_action == 'n':
        user_resume = False
    else:
        print("Invalid Input")

# Computer's turn
while calculate_score(computer_cards) < 17:
    computer_cards += random.choices(cards, k=1)
    update_ace(computer_cards)


# Determine winner
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

# Check the winner condition
if user_score > 21 or (21 >= computer_score > user_score):
    print("You loose")
elif computer_score > 21 or (21 >= user_score > computer_score):
    print("You win")
else:
    print("Draw")
