import random


def choose_word():
    words = ["aeroplane", "engineering", "python", "hangman", "aircraft", "design"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def display_hangman(attempts):
    stages = [
        r"""
           ----
           |  |
           |  O
           | /|\
           | / \
           |
        """,
        r"""
           ----
           |  |
           |  O
           | /|\
           | /
           |
        """,
        r"""
           ----
           |  |
           |  O
           | /|\
           |
           |
        """,
        r"""
           ----
           |  |
           |  O
           | /|
           |
           |
        """,
        r"""
           ----
           |  |
           |  O
           |  |
           |
           |
        """,
        r"""
           ----
           |  |
           |  O
           |
           |
           |
        """,
        r"""
           ----
           |  |
           |
           |
           |
           |
        """
    ]
    print(stages[attempts])


def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Maximum incorrect guesses allowed

    print("Welcome to Hangman!")

    while attempts > 0:
        display_hangman(attempts)
        print("\nWord: ", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good job! That letter is in the word.")
            if set(word).issubset(guessed_letters):
                print("\nCongratulations! You guessed the word:", word)
                return
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts remaining.")

    display_hangman(attempts)
    print("\nGame over! The word was:", word)


if __name__ == "__main__":
    hangman()
