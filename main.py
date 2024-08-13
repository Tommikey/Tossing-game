import random
# A number guessing game.
# the computer will randomly choose a number between 1 and 10
# The player will guess what number it is.
# The player has maximum of 3 guesses.
# If the player guesses right before maximum number of guess. Wins
# If the player can't guess right until maxmimum retries. Lose.
# If player loses, show them the number the computer guessed.
# write a function that tells users if their guess is too low or too high
# Include a margin of +/- 2 or 3 to give a very close or too high/low message
# Claude ai


def number_guessing_game():
    print("Welcome to the random guessing game\n")
    print("Guess a number from 1 to 20")

    MAX_GUESSES = 3
    computer_number = random.randint(1, 20)
    number_of_guesses = 0


    def validate_user_input(number: int) -> bool:
        if user_guessed_number < 1 or user_guessed_number > 20:
            return 1 <= number <= 20

    def give_hint(guess, target):
        if abs(guess - target) <= 2:
            return "Very close!"
        elif guess < target:
            return "Too low!"
        else:
            return "Too high!"
    
    while number_of_guesses < MAX_GUESSES:
        try:
            user_guessed_number = int(input("Attempt a guess: "))
            number_of_guesses += 1

            ...
            if user_guessed_number == computer_number:
                print(f"Correct guess, You are a genius! You guessed it in {number_of_guesses} tries")
                return
            ...
            hint = give_hint(user_guessed_number, computer_number)
            print(f"{hint} You have {MAX_GUESSES - number_of_guesses} guesses left.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Sorry, You've run out of guesses. The computer's number is: {computer_number}")
    print(f"You guessed : {number_of_guesses} times")


number_guessing_game()
