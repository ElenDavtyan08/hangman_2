from funcs_for_game import read_json, get_valid_word, user_input, display_info, check_letter, ALPHABET

data = read_json('hangman/words.json')
words = data["hangmanwords"] 
WORD = get_valid_word(words)
WORD_LETTERS = set(WORD)
USED_LETTERS = set()


def hangman():
    LIVES = 7
    while len(WORD_LETTERS) > 0 and LIVES > 0:
        display_info(LIVES, USED_LETTERS, WORD)
        user_letter = user_input(USED_LETTERS)
        USED_LETTERS.add(user_letter)
        if not check_letter(user_letter, WORD_LETTERS):
            LIVES -= 1
            print('\nYour letter,', user_letter, 'is not in the word.')

    if LIVES == 0:
        print('You died, sorry. The word was', WORD)
    else:
        print('YAY! You guessed the word', WORD, '!!')
