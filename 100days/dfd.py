import random



def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """ take a list and return a calculate score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose! opponent has Blackjack"
    elif user_score == 0:
        return "You Win! You have Blackjack"
    elif user_score >= 21:
        return "you lose"
    elif computer_score > 21:
        return "You Win,opponent went over"
    elif user_score > computer_score:
        return "You win"
    else:
        return "you lose"


def play_game():

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        new_card = deal_card()
        computer_cards.append(new_card)
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards},score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 and user_score > 21:
            is_game_over = True
        else:
            deal = input("Draw another card type 'yes' or End the game type 'no'")
            if deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("You want to Play or quit the game: Type 'y or 'n'") == 'y':
    # clear()
    play_game()