#Name: Min Jung
#Due Date: November 7, 2021
#Assignment 5: Lab 1

user_input= input("Enter a line of English sentence: ")
sep_words = user_input.split()
total_letters = 0
for words in sep_words:
    for letters in words:
        if 'a' <= letters <= 'z' or 'A' <= letters <= 'Z':
            total_letters += 1
print(total_letters)
    