import random
from randomWord import words

import string

def get_valid_word(words):
  word = random.choice(words)
  while '_' in word or ' ' in word:
    word = random.choice(words)
  return word


def hangman():
  
  word = get_valid_word(words)
  word_letters = set(word)
  print(word)
  alphabet = set(string.ascii_uppercase)
  used_letters = set()

  #Getting user input
  while len(word_letters) > 0:
    #letter used
    print("You have used these letters:", ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '_' for letter in word]
    print("Current word",' '.join(word_list))

    
    user_letter= input("Guess letter: ").upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
    elif user_letter in used_letters:
    
      print('You have already used this letter:')
    else:
      print('Invalid character')

 
hangman()