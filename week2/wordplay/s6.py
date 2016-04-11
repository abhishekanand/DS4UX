import scrabble

TheOne = ""
Vowels = ["a", "e", "i", "o", "u"]

for word in scrabble.wordlist:
    hasVowels=False
    for letter in word:
        if letter in Vowels:
            hasVowels=True
    if hasVowels==False and len(word)>len(TheOne):
        TheOne=word
print(TheOne)