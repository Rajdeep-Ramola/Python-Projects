import random
from Hangman_words import word_list
from Hangman_art import logo, stages

print(logo)

# Pick a random word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game state variables
lives = len(stages) - 1
display = ["_" for _ in range(word_length)]
guessed_letters = []

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'")
        continue
    else:
        guessed_letters.append(guess)

    # Check guessed letter
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    # Incorrect guess
    if guess not in chosen_word:
        print(f"'{guess}' is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose! The word was:", chosen_word)

    # Display progress
    print(" ".join(display))
    print(stages[lives])

    # Win condition
    if "_" not in display:
        end_of_game = True
        print("You win!")
