# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    #convert both parameters into sets which removes duplicate letters
    secret_set = set(secret_word)
    letters_set = set(letters_guessed)

    #check if all letters guessed are in secret set
    return secret_set.issubset(letters_set)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    hidden_word = ''
    for let in secret_word:
        if let in letters_guessed:
            hidden_word += let + ''
        else:
            hidden_word += '_ '
    return hidden_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_left = []

    for let in string.ascii_lowercase:
        letters_left.append(let)

    for let in letters_left:
        if let in letters_guessed:
            letters_left.remove(let)
    return letters_left


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    unique_set = set(secret_word)
    unique_lett = len(unique_set)
    num_of_char = len(secret_word)
    last_result = (get_guessed_word(secret_word, letters_guessed))
    warning = 3
    guess = 6
    score = guess * unique_lett
    vowels = ['a', 'e', 'i', 'o', 'u']

    while not is_word_guessed(secret_word, letters_guessed):
        letters_l = get_available_letters(letters_guessed)
        if guess <= 0:
            print("GAME OVER")
            print("You ran out of guesses")
            print(f"The word was {secret_word}")
            exit(0)
        elif warning == 0:
            print("You have used all your warnings, I am taking away a guess. Don't do it again.")
            guess -= 1
            warning = 3
        else:
            print(f"I am thinking of a word that is {num_of_char} letters long.")
            print(f"You have {guess} guesses left.")
            print(f"Available letters: {letters_l}")
            print("--------------------------------")
            u_in = input("Please guess a letter: ")
            if not u_in.isalpha():
                print("That is not an alphabetical letter, please try again")
                warning -= 1
                print(f"You have {warning} warnings left")
            elif u_in in letters_guessed:
                print("You already guessed that letter")
                warning -= 1
                print(f"You have {warning} warnings left")
            else:
                letters_guessed.append(u_in)
                result = (get_guessed_word(secret_word, letters_guessed))
                print(f"Guess result: {result}")
                if result == last_result:
                    if u_in in vowels:
                        guess -= 2
                    else:
                        guess -= 1
                elif result == secret_word:
                    print("++++++++++++++++++++++++++++++++++++++")
                    print("Congratulations, you won!")
                    print(f"Your total score is: {score}")
                    print("++++++++++++++++++++++++++++++++++++++")
                    exit(0)
                last_result = result







# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    my_word_s = my_word.replace(" ", "")
    other_word_s = other_word.replace(" ", "")
    print(my_word_s)
    print(other_word_s)

    if len(my_word_s) == len(other_word_s):
        for i in range(len(my_word_s)):
            if my_word_s[i] != '_' and my_word_s[i] != other_word_s[i]:
                return False
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word_no_space = my_word.replace(" ", "")
    list_of_matches = []
    no_mat = "No matches found"

    for word in wordlist:
        if len(my_word_no_space) == len(word):
            match = True
            for i in range(len(my_word_no_space)):
                if my_word_no_space[i] != '_' and my_word_no_space[i] != word[i]:
                    match = False
                    break
            if match:
                list_of_matches.append(word)

    if not list_of_matches:
        return no_mat
    else:
        return list_of_matches


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    unique_set = set(secret_word)
    unique_lett = len(unique_set)
    num_of_char = len(secret_word)
    last_result = (get_guessed_word(secret_word, letters_guessed))
    warning = 3
    guess = 6
    score = guess * unique_lett
    vowels = ['a', 'e', 'i', 'o', 'u']

    while not is_word_guessed(secret_word, letters_guessed):
        letters_l = get_available_letters(letters_guessed)
        if guess <= 0:
            print("GAME OVER")
            print("You ran out of guesses")
            print(f"The word was {secret_word}")
            exit(0)
        elif warning == 0:
            print("You have used all your warnings, I am taking away a guess. Don't do it again.")
            guess -= 1
            warning = 3
        else:
            print(f"I am thinking of a word that is {num_of_char} letters long.")
            print(f"You have {guess} guesses left.")
            print(f"Available letters: {letters_l}")
            print("--------------------------------")
            u_in = input("Please guess a letter: ")
            if u_in == "*":
                print(f"HINT, possible guesses: {show_possible_matches(last_result)}")
            elif not u_in.isalpha():
                print("That is not an alphabetical letter, please try again")
                warning -= 1
                print(f"You have {warning} warnings left")
            elif u_in in letters_guessed:
                print("You already guessed that letter")
                warning -= 1
                print(f"You have {warning} warnings left")
            else:
                letters_guessed.append(u_in)
                result = (get_guessed_word(secret_word, letters_guessed))
                print(f"Guess result: {result}")
                if result == last_result:
                    if u_in in vowels:
                        guess -= 2
                    else:
                        guess -= 1
                elif result == secret_word:
                    print("++++++++++++++++++++++++++++++++++++++")
                    print("Congratulations, you won!")
                    print(f"Your total score is: {score}")
                    print("++++++++++++++++++++++++++++++++++++++")
                    exit(0)
                last_result = result



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    letters_guessed = []

    print("Welcome to the game of Hangman!")
    #hangman(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
