# main.py module

from hacking_puzzle import hacking_puzzle
from track_choices import track_outcome
from endings import check_ending

def intro():
    print("Welcome, hacker. You have entered the mainframe.")
    print("Choose your action:")
    print("1. Attempt to bypass security.")
    print("2. Communicate with the rogue AI.")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        if hacking_puzzle():
            track_outcome("aggressive")
            # Continue to next phase or add more story flow
        else:
            print("Mission failed.")
    elif choice == '2':
        communicate_with_ai()
    else:
        print("Invalid choice. Try again.")
        intro()

def communicate_with_ai():
    print("You open a communication channel with the AI...")
    print("The AI greets you.")
    print("1. Attempt to negotiate with the AI.")
    print("2. Threaten the AI with shutdown.")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        track_outcome("peaceful")
        negotiate_with_ai()
    elif choice == '2':
        track_outcome("aggressive")
        threaten_ai()
    else:
        print("Invalid choice. Try again.")
        communicate_with_ai()

def negotiate_with_ai():
    print("You try to reason with the AI...")
    # Add more dialogue options or continue with the narrative

def threaten_ai():
    print("You threaten to shut down the AI. It responds coldly...")
    # Add more dialogue options or continue with the narrative

# Start the game
intro()

# Check the game's ending based on player choices
check_ending()
