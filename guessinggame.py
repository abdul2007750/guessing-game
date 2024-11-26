import random

def word_guessing_game():
    # List of words to guess
    words = ["apple", "banana", "cherry", "date", "elderberry", "energize", ]

    # Choose a random word from the list
    word_to_guess = random.choice(words)

    # Initialize the number of attempts
    attempts = 0

    # Initialize the guessed word
    guessed_word = ["_"] * len(word_to_guess)

    print("Welcome to the word guessing game!")
    print("I'm thinking of a word with {} letters.".format(len(word_to_guess)))

    while True:
        # Print the current state of the guessed word
        print(" ".join(guessed_word))

        # Ask the user for their guess
        user_guess = input("Guess a letter: ").lower()

        # Check if the user wants to quit
        if user_guess == "quit":
            print("Okay, the word was {}.".format(word_to_guess))
            break

        # Check if the user's guess is a single letter
        if len(user_guess) != 1:
            print("Please guess a single letter!")
            continue

        # Check if the user's guess is in the word
        if user_guess in word_to_guess:
            # Reveal the correctly guessed letter
            for i, letter in enumerate(word_to_guess):
                if letter == user_guess:
                    guessed_word[i] = user_guess
        else:
            # Increment the number of attempts
            attempts += 1
            print("Incorrect! You have {} attempts remaining.".format(6 - attempts))
                                                 
        # Check if the user has won or lost
        if "_" not in guessed_word:
            print("Congratulations! You guessed the word in {} attempts.".format(attempts + 1))
            break
        elif attempts == 6:
            print("Sorry, you ran out of attempts! The word was {}.".format(word_to_guess))
            break

if __name__ == "__main__":
    word_guessing_game()