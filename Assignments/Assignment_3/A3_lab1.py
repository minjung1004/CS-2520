#Name: Min Jung
#Due Date: October 11, 2021
#CS 2520- Python for Programmers
#Homework #3: Lab 1: Leap Year-Function


input_user_year=int(input("Enter a year:"))

def is_leap_year(user_year):
    leap_year = user_year%400 
    if leap_year == 0 or leap_year%4 == 0:
        print(f'{user_year:.0f} is a leap year.')
    else:
        print(f'{user_year:.0f} is not a leap year.')
      
is_leap_year(input_user_year)

   