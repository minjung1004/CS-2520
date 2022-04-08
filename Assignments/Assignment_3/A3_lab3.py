#Name: Min Jung
#Due Date: October 11, 2021
#CS 2520- Python for Programmers
#Homework #3: Lab 3

def is_list_mult10(my_list):
    if all(x == 0 for x in my_list):
        return True;

def is_list_no_mult10(my_list):
    if all(x != 0 for x in my_list):
        return True;

def main():
    lst = []
    my_list_range = int(input("Enter a list of numbers:"))
    for i in range(0, my_list_range):
        input_my_list = int(input())
        lst.append(input_my_list%10)
    
    if is_list_mult10(lst) == True:
        print("All multiples of 10")
    elif is_list_no_mult10(lst) == True:
        print("No multiples of 10")
    else:
        print("Mixed values")

main()

