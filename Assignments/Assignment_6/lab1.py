#Name: Min Jung
#Due Date: 11/19/2021
#HW:File and Exception #1

import math

argument=float(input('enter a number to square root:'))
class safe:
    def sqrt(argument):
        try:
            return math.sqrt(argument)
        except :
            print('Error: Input a different number')
            return 0.0
print(format(safe.sqrt(argument), '.2f'))