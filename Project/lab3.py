#Name: Min Jung
#Due Date: October 31, 2021
#Project 1: Lab 3

import random

random_num = random.randint(1, 100)

user_num= int(input("Guess the number:"))

guess_count = 0

while user_num != random_num:
    guess_count +=1
    if user_num > random_num:
        print("Too high, try again")
        user_num= int(input("Guess the number:"))
    else:
        print("Too low, try again")
        user_num= int(input("Guess the number:"))

print("Congradulations! You guessed right!!")
print("Total Guesses:", guess_count)

