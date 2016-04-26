# Retrieves square pictures of kittens from the 
# placekitten.com API

import requests

# Gets the user's input to determine picture size
pic_width = input("How wide a kitten? ")
pic_height = input("How tall a kitten? ")

# Creates custom URL for the API
url = "http://placekitten.com/g/%s/%s" % (pic_width, pic_height)

# Requests and gets the photo data
kitten = requests.get(url)

# Saves (writes) the file
file_name = "kitten_%sby%s.jpeg" % (pic_width, pic_height)
kitten_file = open(file_name, "wb")
kitten_file.write(kitten.content)
kitten_file.close()
