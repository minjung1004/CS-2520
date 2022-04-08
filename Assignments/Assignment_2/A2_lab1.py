#Min Jung
#09/22/2021
#Homework #2: Lab 1

#takes int in range 11-100 as input
#out put is a countdown starting from the int input
#stop output when the digits are identical ex 11, 22, 33, 44, 55, etc

user_input = int(input("Enter a number between 11-100: "))


while 11 <= user_input <= 100:
    print(user_input)
    if user_input % 11 == 0:   #finds the identical digits, which are all perferctly divisble by 11    
        break
    user_input -= 1 
else:
    print("Input must be 11-100")
        
