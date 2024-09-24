# endings.py module
from track_choices import get_aggressive_actions, get_peaceful_actions

def check_ending():
    aggressive = get_aggressive_actions()
    peaceful = get_peaceful_actions()
    
    if aggressive > peaceful:
        print("The AI views you as an enemy and initiates a world takeover. Game over.")
    elif peaceful > aggressive:
        print("You have successfully negotiated peace with the AI. Humanity and AI coexist.")
    else:
        print("The future is uncertain, neither side has fully won. The world waits.")
