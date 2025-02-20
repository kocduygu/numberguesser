def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    print("Please respond with 'higher', 'lower', or 'correct' based on my guesses.\n")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        response = input(f"Is your number {guess}? (higher/lower/correct): ").strip().lower()

        if response == "correct":
            print(f"Yay! I guessed your number in {attempts} attempts!")
            break
        elif response == "higher":
            low = guess + 1
        elif response == "lower":
            high = guess - 1
        else:
            print("Invalid input. Please respond with 'higher', 'lower', or 'correct'.")
    else:
        print("Hmm, it seems like there was a misunderstanding. Let's try again!")

if __name__ == "__main__":
    guess_number()