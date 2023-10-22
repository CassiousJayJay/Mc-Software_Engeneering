import random

lower = 1
upper = 50
attempts = 5

secrete_number = random.randint(lower, upper)

def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower} and {upper}: "))
            if lower <= guess <= upper:
                return guess
            else:
                print("Invalid input. Please enter a valid input within a specified range.")
        except ValueError:
            print("Please enter a valid number.")
            
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"
    
def play_game():
    attempts = 0
    won = False
    
    while attempts < attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secrete_number)
        
        if result == "Correct":
            print(f"Congratulations! You guessed the secrete number {secrete_number} in attempts {attempts}")
            won = True
        
        else:
            print(f"{result}. Try Again")
    if not won:
        print(f"Sorry you ran out of attempts, the secrete number is {secrete_number}.")
        
if __name__=="__main__":
    play_game()