"""
It uses the concepts that we just reviewed (random, range, input, and while) to build a math guessing game.
random.choice, range, input, while, and join.

This program asks people to add together two random numbers between 1 and 1000, and keep asking them new questions as long as they gave the answer right to the previous math problem. Once they give an incorrect answer, it prints out how many they got right, and also prints all their correct responses using join.
"""
import random

numbers_to_add = list(range(1,1001))
correct_answers = []
true_answer = 0
your_answer = 0
while true_answer == your_answer:
    num1 = random.choice(numbers_to_add)
    num2 = random.choice(numbers_to_add)
    true_answer = num1 + num2
    your_answer = int(input("%d + %d = " % (num1,num2)))
    if your_answer == true_answer:
        print("Correct! Let's try another.")
        correct_answers.append("%d + %d = %s" % (num1, num2, your_answer))
    else:
        print("Incorrect!")

print("You got %d problems right:" % (len(correct_answers)))
print(", ".join(correct_answers))
