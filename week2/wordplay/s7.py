# Find an print the words that contain 4 or more 'l's.
import scrabble

for word in scrabble.wordlist:
    if (word.count('l')>= 4):
        print (word)
