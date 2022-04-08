#Min Jung
#09/22/2021
#Homework #2: Lab 2

user_input= input("Enter input:\n")

new_string = ""    #intialize new string

for char in user_input:
    if ord(char) >= 65 and ord(char) <=90:        #use ASCII
        new_string += char
    elif ord(char) >= 97 and ord(char) <=122:
        new_string += char
        
print("Number of characters:", len(new_string))

#print(len(remove_space))

