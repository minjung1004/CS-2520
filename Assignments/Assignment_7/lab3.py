#Name: Min Jung
#Due Date: 11/30/2021
#Homework Assignment on Classes and Objects: Lab 3
from math import tan, pi

class Polygon:
    def __init__(self, n_sides, length):
        self.n_sides = n_sides
        self.length = length
    def perimeter(self):
        self.perimeter = self.n_sides * self.length
        print(f'Perimeter: {self.perimeter:.2f}')
    def area(self):
        self.area = self.n_sides * (self.length ** 2 ) / (4 * tan (pi / self.n_sides))
        print(f'Area: {self.area:.2f}')                                        
    
    
def main():
    n_sides=int(input("Enter the number of sides: "))
    length = int(input("Enter the length of the sides: "))
    results = Polygon(n_sides, length)
    results.perimeter()
    results.area()
main()
