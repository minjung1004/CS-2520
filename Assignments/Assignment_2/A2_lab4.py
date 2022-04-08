#Min Jung
#09/22/2021
#Homework #2: Lab 4

'''
  i becomes 1
  a becomes @
  m becomes M
  B becomes 8
  s becomes $
'''
user_input= input("Enter password: ")

for char in user_input:
    user_input = user_input.replace('i' , '1').replace('a','@').replace('m','M').replace('B', '8').replace('s', '$')
    print(user_input + '!')
    break

'''
#Another way, using .translate and .maketrans instead of .replace
change_char ={'i':'1', 'a':'@','m':'M','B':'8','s':'S'}
for char in user_input:
    user_input=user_input.translate(str.maketrans(change_char))
    print(user_input+'!')
    break

#Doing using while-loop

 while user_input:
    new_string = user_input.replace('i' , '1').replace('a','@').replace('m','M').replace('B', '8').replace('s', '$')
    print(new_string + '!')
    break
'''

