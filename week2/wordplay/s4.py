import scrabble

longword = []
length = []
vowel = ['a','e','i','o','u']
for item in scrabble.wordlist:   
    if (vowel in item == False):    
        longword.append(item)
        length.append(len(item))
    else:
        pass


for word in longword:
    if(len(word)== max(length)):
        print(word)