# hacking_puzzle.py module

def hacking_puzzle():
    password = "open_sesame"
    attempts = 3
    
    while attempts > 0:
        guess = input("Enter the password to bypass security: ")
        if guess == password:
            print("Access granted!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts remaining.")
    
    if attempts == 0:
        print("System locked. You're caught by security.")
        return False
