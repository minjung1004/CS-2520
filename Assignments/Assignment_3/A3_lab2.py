#Name: Min Jung
#Due Date: October 11, 2021
#CS 2520- Python for Programmers
#Homework #3: Lab 2: A jiffy

input_user_seconds= int(input("Enter a number of seconds:"))

def seconds_to_jiffies(user_seconds):
    jiffies = user_seconds * 100
    print('{:.2f}'.format(jiffies))

seconds_to_jiffies(input_user_seconds)