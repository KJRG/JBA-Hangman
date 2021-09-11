# Write your code here

from random import choice
from string import ascii_lowercase


POSSIBLE_SECRET_WORDS = ["python", "java", "kotlin", "javascript"]
INITIAL_NUMBER_OF_LIVES = 8


def create_guessing_state(word, visible_letters):
    letters = [letter if letter in visible_letters else "-" for letter in word]
    return "".join(letters)


def validate_input(user_input):
    if len(user_input) != 1:
        return False, "You should input a single letter"
    if user_input not in ascii_lowercase:
        return False, "Please enter a lowercase English letter"
    return True, ""


def play_game():
    secret_word = choice(POSSIBLE_SECRET_WORDS)
    correctly_guessed_letters = set()
    all_entered_letters = set()
    guessing_state = create_guessing_state(secret_word, correctly_guessed_letters)
    lives_left = INITIAL_NUMBER_OF_LIVES
    while lives_left > 0:
        print()
        print(guessing_state)
        user_guess = input("Input a letter: ")
        is_input_valid, validation_msg = validate_input(user_guess)
        if is_input_valid:
            if user_guess in all_entered_letters:
                print("You've already guessed this letter")
                continue
            all_entered_letters.add(user_guess)
            if user_guess in secret_word:
                correctly_guessed_letters.add(user_guess)
                guessing_state = create_guessing_state(secret_word, correctly_guessed_letters)
            else:
                lives_left -= 1
                print("That letter doesn't appear in the word")
            if guessing_state == secret_word:
                print(f"You guessed the word {secret_word}!")
                print("You survived!")
                break
        else:
            print(validation_msg)
    else:
        print("You lost!")


print("H A N G M A N")
user_menu_input = ""
while True:
    user_menu_input = input('Type "play" to play the game, "exit" to quit: ')
    if user_menu_input == "exit":
        break
    elif user_menu_input == "play":
        play_game()
    print()
