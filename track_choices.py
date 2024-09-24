# track_choices.py module

# Variables to track player's behavior
aggressive_actions = 0
peaceful_actions = 0

def track_outcome(choice):
    global aggressive_actions, peaceful_actions
    
    if choice == "aggressive":
        aggressive_actions += 1
        print("Aggressive action noted.")
    elif choice == "peaceful":
        peaceful_actions += 1
        print("Peaceful action noted.")

def get_aggressive_actions():
    return aggressive_actions

def get_peaceful_actions():
    return peaceful_actions
