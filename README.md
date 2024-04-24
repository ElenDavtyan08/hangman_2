# Hangman 2
Here is the second version of hangman game, but it is built with functions, which make code more readbale.

### Rules
Initially, you start with 7 lives. A word is presented to you in the form of dashes representing each letter (e.g., '----' for a 4-letter word). If you correctly guess a letter, it replaces the corresponding dash in the word. However, if your guess is incorrect, the letter is displayed among the incorrect guesses, and one life is deducted. Repeatedly guessing the same letter results in a warning: 'You have already used that letter. Guess another letter.' The game proceeds until you exhaust your lives or correctly guess the word.

### Files: funcs_for_game.py, game.py, main.py and words.json.
* __funcs_for_game.py__ -> here are functions that are used in further for making the main hangman function
* __game__.py -> here is the hangman function, where is built hangman function with functions from previous file
* __main__.py -> here is inserted the main hangman function and this is the main file, where you need to play

\
Now let's start to test and play it!
