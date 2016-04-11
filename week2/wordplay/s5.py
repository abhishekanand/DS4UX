# Find and print the words that have all 5 vowels in alphabetical order.

import scrabble
vowels = ['a', 'e', 'i', 'o', 'u']
for word in scrabble.wordlist:
    count = 0
    for vowel in range(0,4):
        if vowels[vowel] in word and vowels[vowel+1] in word:
            if word.index(vowels[vowel]) < word.index(vowels[vowel+1]):
                count = count + 1
    if count == 4:
        print(word)
