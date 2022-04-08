#Min Jung
#09/22/2021
#Homework #2: Lab 3- Brute force equation solver

#Ax + By = C
A1 = int(input())
B1 = int(input())
C1 = int(input())

A2 = int(input())
B2 = int(input())
C2 = int(input())


for x in range(-10,10):
    for y in range(-10,10):
        if (A1 * x) + (B1 * y) == C1 and (A2 * x) + (B2 * y) == C2:       
             print('x= {}, y= {}'.format(x,y))  
             break
    else:
        continue
    break
else:
    print("There is no solution")
    
    