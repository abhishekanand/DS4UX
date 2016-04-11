import scrabble
vowels = ['a', 'e', 'i', 'o', 'u']
words=[]
for word in scrabble.wordlist:
    vowel = False
    for letter in word:
        if letter in vowels:
            vowel = True
    if not vowel:
        words.append(word)
print(max(words, key=len))