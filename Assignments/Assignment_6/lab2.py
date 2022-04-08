#Name: Min Jung
#Due Date: 11/19/2021
#HW:File and Exception #2

import math

class safe:
    def sqrt():
        try:
            fp = open("data.txt", "r")
            print("Squared values:")
            for number in fp:
                number = float(number)
                print(format(math.sqrt(number), '.2f'))
            fp.close()
        except IOError :
            print('Error: File cannot be read')
        except:
            print("Error: File has input that is not a number or that is not positive. Please check the file.")
print(safe.sqrt())

