import random
import pickle

def start_game():
    # Checks for a saved game
    if load_game():
        answer = input("Do you want to load your saved game? (yes/no): ")
        if answer.lower() == "yes":
            print("Loading saved game...")
            question_1()
            return

    # If there is no saved game or the player said not to load it. Start a new game.
    print("You wake up in a dark room. You hear footsteps approaching. What do you do?")
    # This function represents two options to hide under the bed or to find the door.
    # Each options has a chance of failing but will lead you to the hallway.
    # If you enter a wrong choice it will ask you to try again
    print("1. Hide under the bed.")
    print("2. Try to find a way out through the door.")
    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        hide_under_bed()
    elif choice == '2':
        find_a_way_out()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def hide_under_bed():
    # This function represents the option to hide under the bed. There is a random chance that the killer finds you.
    while True:
        print("You hide under the bed. The killer enters the room and looks around.")
        if random.randint(0, 1) == 0:
            print("The killer finds you and captures you. You where stab to death. Game over")
            break
        else:
            print("The killer doesn't find you. You manage to escape.")
            question_1()
            break

def find_a_way_out():
    # This function shows you try to find the door. Once you get to the door there is a chance it is locked.
    print("You try to find a way out through the door.")
    if random.randint(0, 1) == 0:
        print("The door is locked. The killer finds you and captures you. He chomps of your fingers while you watch. Game Over")
    else:
        print("You find the door unlocked. You escape and call the cops.")
        question_1()

def question_1():
    # This fuction goes over the hallway choise. Once you choose you will be asked another question.
    answer = input("You find yourself in a hallway. Which way do you go? (left/right): ")
    if answer.lower() == "left":
        question_2()
    else:
        question_3()

def question_2():
    # This goes over if you chose left at the hallway. You will be asked to pick the lock.
    # If you say yes there is a chance you fail and eill be killed. If you say no you will be killed
    answer = input("You encounter a locked door. Do you try to pick the lock? (yes/no): ")
    if answer.lower() == "yes":
        if random.randint(0, 1) == 0:
            print("You successfully pick the lock and escape. Congratulations! You survived.")
            play_again()
        else:
            print("You fail to pick the lock. The killer finds you and captures you. He laughs while choping your legs off. Game over.")
    else:
        print("You decide not to risk it. You turn back and encounter the killer. He takes his knife and slice your head off. Game over.")

def question_3():
    # This goes over the option of right. You will find a staircase.
    # If choose not to go down the game is over.
    answer = input("You see a staircase going down. Do you take it? (yes/no): ")
    if answer.lower() == "yes":
        question_4()
    else:
        print("You decide to stay on the current floor. The killer finds you. Game over.")

def question_4():
    # You will find a broken door. If you choose to break it you will be free. But there a chance it will fail
    # otherwise you go to the next choice.
    answer = input("You find a broken door. Do you try to break it and escape? (yes/no): ")
    if answer.lower() == "yes":
        if random.randint(0, 1) == 0:
            print("You successfully break the door and escape. Congratulations! You survived.")
            play_again()
        else:
            print("You fail to break the door. The noise alerts the killer. He finds a nice place for your head on his shelf. Game over.")
    else:
        question_5()

def question_5():
    # You find a phone. If you choose to use it the police will gun down killer. However there a chance that it could fail
    # If you choose not to you will die
    answer = input("You find a phone. Do you call the police? (yes/no): ")
    if answer.lower() == "yes":
        if random.randint(0, 1) == 0:
            print("The police arrive and killed the killer. Congratulations! You survived.")
            play_again()
        else:
            print("The killer hears you and captures you before you can make the call. He eats your dead body. Game over.")
    else:
        print("You choose not to call the police. The killer finds you. He then throws knifes at your head until he hits you. Game over.")

def take_direction(direction):
    # A failed function I tried to use
    print(f"You choose to go {direction}.")
    return direction

def get_random_number():
    # A failed function I tried to use
    return random.randint(1, 100)

def save_game():
    # How I save the game
    with open("savegame.pickle", "wb") as save_file:
        pickle.dump(True, save_file)

def load_game():
    # How I load the game
    try:
        with open("savegame.pickle", "rb") as save_file:
            return pickle.load(save_file)
    except FileNotFoundError:
        return False

def play_again():
    # The choice to play again
    answer = input("Do you want to play again? (yes/no): ")
    if answer.lower() == "yes":
        start_game()
    else:
        print("Thanks for playing!")

start_game()









