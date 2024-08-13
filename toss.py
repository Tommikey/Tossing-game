import random

def number_guessing_game():
    print("Welcome to the random guessing game\n")
    print("Guess a number from 1 to 20")

    computer_number = random.randint(1, 20)
    MAX_GUESSES = 4
    number_of_guesses = 0

    while number_of_guesses < MAX_GUESSES:
        try:
            user_guessed_number = int(input("Attempt a guess: "))
            number_of_guesses += 1

            if user_guessed_number < 1 or user_guessed_number > 20:
                print("Invalid range. Please guess a number between 1 and 20.")
                continue

            if user_guessed_number == computer_number:
                print(f"Correct guess! You are a genius! You guessed it in {number_of_guesses} tries.")
                return

            hint = give_hint(user_guessed_number, computer_number)
            print(f"{hint} You have {MAX_GUESSES - number_of_guesses} guesses left.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Sorry, you've run out of guesses. The computer's number was: {computer_number}")

def give_hint(guess, target):
    if abs(guess - target) <= 2:
        return "Very close!"
    elif guess < target:
        return "Too low!"
    else:
        return "Too high!"


number_guessing_game()
