import random
import logging
import json
import string

ALPHABET = set(string.ascii_uppercase)

def read_json(source: str):   # json file reader made by ArtyoMKo
    try:
        with open(source, "r", encoding="utf-8") as read_file:
            data = json.load(read_file)
        return data
    except FileNotFoundError:
        logging.error(f"{source} file not found")
        raise FileNotFoundError
    
def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display_info(lives, used_letters, word):
    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

def check_letter(user_letter, word_letters):
    if user_letter in word_letters:
        word_letters.remove(user_letter)
        return True
    else:
        return False
    
def user_input(used_letters):
    while True:
        user_letter = input('Guess a letter: ').upper()
        if user_letter in string.ascii_uppercase and user_letter not in used_letters:
            return user_letter
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')
        else:
            print('\nThat is not a valid letter.')