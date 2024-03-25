import tkinter as tk
import random
# Made a poker game using tkinter thought it would be a fun way to kill some time after the fire
class PokerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker")
        
        # Create deck and player's hand
        self.deck = self.create_deck()
        self.player_hand = []
        
        # My GUI elements
        self.title_label = tk.Label(root, text="Welcome to Poker", font=("Helvetica", 16))
        self.title_label.pack()
        
        self.deal_button = tk.Button(root, text="Deal Hand", command=self.deal_hand)
        self.deal_button.pack()
        
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    
    # How I made the deck
    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return [(value, suit) for suit in suits for value in values]
    
    def deal_hand(self):
        # Allows me to Reset player's hand
        self.player_hand = []
        
        # This will Shuffle deck
        random.shuffle(self.deck)
        
        # This deal 5 cards to player
        self.player_hand = self.deck[:5]
        self.deck = self.deck[5:]
        
        # This shows player's hand
        hand_str = ", ".join(f"{value} of {suit}" for value, suit in self.player_hand)
        self.result_label.config(text=f"Your hand: {hand_str}")

# This will make main window
root = tk.Tk()
app = PokerApp(root)

#  This will run the application
root.mainloop()










