

import scrabble

# Find and print the words that start with "ee".
print (" # Find and print the words that start with 'ee'.  ")

print (" Solution 1 ")
for item in scrabble.wordlist:
    if item[0]== "e" and item[1] == "e":
        print (item)
    else:
        pass

print ("  ")
print (" Solution 2 ")
for item in scrabble.wordlist:
    if item[:2] == "ee": # item[0:2]
        print (item)
    else:
        pass

print ("  ")
print (" Solution 3 ")
for item in scrabble.wordlist:
    if item.startswith("ee"):
        print (item)
    else:
        pass



print ("--------------End-----------")
print ("  ")
# Find and print the words that end in "mt". How about "gry"?

print (" # Find and print the words that end in 'mt'. How about 'gry'? ")
print (" Solution 1 ")
for item in scrabble.wordlist:
    if item.endswith("mt"):
        print (item)
    else:
        pass

print ("  ")
print (" Solution 2 ")
for item in scrabble.wordlist:
    if item[-2] == "m" and item[-1] == "t":
        print (item)
    else:
        pass

print ("  ")
print (" Solution 3 ")
for item in scrabble.wordlist:
    if item[-2:]== "mt":
        print (item)
    else:
        pass

print ("  ")
print (" Solution : Ends with 'gry' ")
for item in scrabble.wordlist:
    if item.endswith("gry"):
        print (item)
    else:
        pass


print ("--------------End-----------")
print ("  ")


# Find and print the longest word that has no vowels.
print (" # Find and print the longest word that has no vowels. ")
print ("  ")
print (" Solution 1 ")
longword = []
length = []

for item in scrabble.wordlist:
    if ('a' in item or 'e' in item or 'i' in item or 'o' in item or 'u' in item) == False:
        longword.append(item)
        length.append(len(item))
    else:
        pass

# print max(longword,max(length))
for word in longword:
    if(len(word)== max(length)):
        print(word)


print ("--------------End-----------")
print ("  ")

# Find an print the words that contain 4 or more 'l's.
print (" # Find an print the words that contain 4 or more 'l's. ")
for word in scrabble.wordlist:
    if (word.count('l')>= 4):
        print (word)

print ("--------------End-----------")

# Find and print the words that have all 5 vowels in alphabetical order.
print (" # Find and print the words that have all (only) 5 vowels in alphabetical order. ")
print ("  ")

VOWELS  = ["a","e","i","o","u"]
for word in scrabble.wordlist:
    found_vowels = []

    for letter in word:
        if letter in VOWELS:
            found_vowels.append(letter)

    if found_vowels == VOWELS:
        print(word)

print ("--------------End-----------")
print ("  ")
# Look for other interesting properties of English words in pages like this quiz asking to find English words with unusual properties. How many can you solve with Python?
print (" Look for other interesting properties of English words in pages like this quiz asking to find English words with unusual properties. How many can you solve with Python? ")
print ("--------------End-----------")
print ("  ")
