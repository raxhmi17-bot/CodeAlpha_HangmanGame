
import random

words = ["apple", "python", "mango", "tiger", "hello"]

word = random.choice(words)

guessed = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed:
        print("You already guessed this letter!")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Game over!")
    print("The word was:", word)
