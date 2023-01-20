#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Problem 1

'1A) Determine whether the word has been guessed'

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True


# In[2]:


# Problem 2

'1B) Getting the user’s guess'

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = []
    for i in secretWord:
        if i in lettersGuessed:
            result.append(i)
        else:
            result.append('_')
    return ' '.join(result)


# In[3]:


# Problem 3

'1B) Getting all available letters'

import string
alph = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    remain = []
    for i in alph:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)


# In[4]:


# Problem 4

# The Game

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many
      letters the secretWord contains.
      
    * Ask the user to supply one guess (i.e. letter) per round.
    
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
      
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
      
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []

    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('Congratulations, you won!')
            break
        else:
            print('------------')
            print('You have', 8 - mistakesMade, 'guesses left.')
            print('Available letters:', getAvailableLetters(lettersGuessed))
            guess = str(input('Please guess a letter:')).lower()
            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            elif guess not in secretWord:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(guess)
                mistakesMade += 1
        if 8 - mistakesMade == 0:
            print('------------')
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break
        else:
            continue


# In[ ]:




