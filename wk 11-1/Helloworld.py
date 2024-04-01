import tkinter as tk
import random
# I am using my GUI assigment for this task. I added a dictioary to it as to keep track of the player's score, the high score, and the current round number. I've added a dictionary called game_data. The round number and score have been increased by updating the deal_hand method. 
class PokerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Game")
        
        # Creates the deck and player's hand
        self.deck = self.create_deck()
        self.player_hand = []
        
        # MY GUI elements
        self.title_label = tk.Label(root, text="Welcome to Poker Game", font=("Helvetica", 16))
        self.title_label.pack()
        
        self.deal_button = tk.Button(root, text="Deal Hand", command=self.deal_hand)
        self.deal_button.pack()
        
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        # Creates dictionary to store game data
        self.game_data = {
            'round': 1,
            'score': 0,
            'high_score': 0
        }
    
    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return [(value, suit) for suit in suits for value in values]
    
    def deal_hand(self):
        # changes player's hand
        self.player_hand = []
        
        # Shuffle the deck
        random.shuffle(self.deck)
        
        # Deal 5 cards to player
        self.player_hand = self.deck[:5]
        self.deck = self.deck[5:]
        
        # Shows player's hand
        hand_str = ", ".join(f"{value} of {suit}" for value, suit in self.player_hand)
        self.result_label.config(text=f"Your hand: {hand_str}")
        
        # Update game data
        self.game_data['round'] += 1
        self.game_data['score'] += 10  # Example: Increase score by 10 for each round
        
        # Update high score if current score is higher
        if self.game_data['score'] > self.game_data['high_score']:
            self.game_data['high_score'] = self.game_data['score']
    
    def display_game_data(self):
        # Shows game data
        game_data_str = f"Round: {self.game_data['round']}\nScore: {self.game_data['score']}\nHigh Score: {self.game_data['high_score']}"
        game_data_label = tk.Label(self.root, text=game_data_str)
        game_data_label.pack()

# Create the main window
root = tk.Tk()
app = PokerApp(root)

# Shows game data
app.display_game_data()

# Run the application
root.mainloop()
