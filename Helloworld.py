import random

def create_deck():
    """Create a deck of cards."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'suit': suit, 'value': value} for suit in suits for value in values]  # Create a list of dictionaries showing cards
    random.shuffle(deck)  # Shuffle the deck
    return deck

def card_value(card):
    """Return the value of a card."""
    if card['value'] in ['Jack', 'Queen', 'King']:
        return 10
    elif card['value'] == 'Ace':
        return 11
    else:
        return int(card['value'])

def hand_value(hand):
    """Calculate the value of a hand."""
    value = sum(card_value(card) for card in hand)  # Sum the values of all cards in the hand
    num_aces = sum(1 for card in hand if card['value'] == 'Ace')  # Count the number of Aces in the hand
    while value > 21 and num_aces:
        value -= 10  # Reduce the value by 10 for each Ace until the value is less than or equal to 21
        num_aces -= 1
    return value

def display_hand(name, hand):
    """Display a player's hand."""
    print(f"{name}'s hand:")
    for card in hand:
        print(f"  {card['value']} of {card['suit']}")

def play_round(balance):
    """Play a round of blackjack."""
    deck = create_deck()  # Create a shuffled deck
    player_hand = [deck.pop(), deck.pop()]  # Deal two cards to the player
    dealer_hand = [deck.pop(), deck.pop()]  # Deal two cards to the dealer

    bet = int(input(f"Enter your bet (Minimum $15, Maximum ${balance}): "))  # Get the player bet amount
    while bet < 15 or bet > balance:  # Validate the bet amount
        bet = int(input(f"Invalid bet amount. Please enter a bet between $15 and ${balance}: "))

    balance -= bet  # Deduct the bet amount from the balance

    print("\nPlayer's Hand:")
    display_hand("Your", player_hand)  # Display the player's hand
    print("\nDealer's Hand:")
    print(f"  {dealer_hand[0]['value']} of {dealer_hand[0]['suit']}")  # Display one of the dealer's cards
    print("  Unknown Card\n")

    if hand_value(player_hand) == 21:  # Check for blackjack
        print("Blackjack! You win 1.5 times your bet!")
        balance += int(bet * 2.5)  # Pay out 1.5 times the bet amount
        return balance

    while True:
        action = input("Do you want to (h)it, (s)tand, or (d)ouble down? ")  # Ask the player for their action
        if action.lower() == 'd':
            if bet * 2 > balance:
                print("Not enough balance to double down.")
                continue
            bet *= 2  # Double the bet amount
            balance -= bet  # Deduct the new bet amount from the balance
            player_hand.append(deck.pop())  # Deal one more card to the player
            display_hand("Your", player_hand)  # show the player's hand
            if hand_value(player_hand) > 21:
                print("You bust! You lose your bet.")
                return balance  # Player busts, return the updated balance
            break
        elif action.lower() == 'h':
            player_hand.append(deck.pop())  # Deal one more card to the player
            display_hand("Your", player_hand)  # Display the player's hand
            if hand_value(player_hand) > 21:
                print("You bust! You lose your bet.")
                return balance  # Player busts, return the updated balance
        elif action.lower() == 's':
            break  # Player stands, exit the loop

    print("\nDealer's Hand:")
    display_hand("Dealer's", dealer_hand)  # Display the dealer hand

    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())  # Dealer hits if hand value is less than 17
        display_hand("Dealer's", dealer_hand)  # Display the dealer hand

    if hand_value(dealer_hand) > 21 or hand_value(player_hand) > hand_value(dealer_hand):
        print("You win!")
        balance += bet * 2  # Player wins, add the bet amount to the balance
        return balance
    elif hand_value(player_hand) < hand_value(dealer_hand):
        print("Dealer wins!")
        return balance - bet  # Dealer wins, deduct the bet amount from the balance
    else:
        print("It's a tie!")
        balance += bet  # Tie, return the bet amount to the balance
        return balance

def blackjack_game():
    """Play 3 rounds of blackjack."""
    balance = 100  # Set the initial balance
    for _ in range(3):  # Play three rounds
        print(f"\nBalance: ${balance}")
        if balance < 15:
            print("Not enough balance to play.")
            break
        balance = play_round(balance)  # Play a round and update the balance
    print(f"\nFinal balance: ${balance}")  # Show the final balance

if __name__ == "__main__":
    blackjack_game()  # Start the game








