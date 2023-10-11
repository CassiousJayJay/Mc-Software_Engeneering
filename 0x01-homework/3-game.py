import random 

lower_bound = 1
upper_bound = 100
max_attempts = 5

secrete_number = random.randint(lower_bound, upper_bound)

def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between{lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid input. Please enter a number within a specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def check_guess(guess, secrete_number):
    if guess == secrete_number:
        return "Correct"
    elif guess < secrete_number:
        return "Too low"
    else:
        return"Too high"
    
def play_game():
    attempts = 0
    won = False
    
    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secrete_number)
        
        if result == "Correct":
            print(f"Congratulations! You guessed the secrete number{secrete_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try again!")
        
    if not won:
            print(f"Sorry you ran out of attempts! The secrete number is {secrete_number}.")
            
if __name__ == "__main__":
    print("Welcome to the Guessing Game!")
    play_game()