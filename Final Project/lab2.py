#Name: Min Jung
#Due Date:12/05/2021
#Final Project: Lab 2

class Triangle:
    def __init__(self, base1, height1, base2, height2):
        self.base1 =base1
        self.height1= height1
        self.base2= base2
        self.height2 = height2
    def compare_area(self):
        self.area1 = 0.5 * self.base1 * self.height1
        self.area2 = 0.5 * self.base2 * self.height2
        if self.area1 > self.area2:
            print(f'Base:{self.base1:.2f}')
            print(f'Height:{self.height1:.2f}')
            print(f'Area:{self.area1:.2f}')
        elif self.area1 == self.area2:
            print("Both Triangles have the same area!")
            print(f'Triangle 1 Area: {self.area1:.2f}')
            print(f'Triangle 2 Area: {self.area2:.2f}')
        else:
            print(f'Base:{self.base2:.2f}')
            print(f'Height:{self.height2:.2f}')
            print(f'Area:{self.area2:.2f}')
def main():
    base1= float(input())
    height1= float(input())
    base2= float(input())
    height2= float(input())
    
    area = Triangle(base1,height1,base2,height2)
    print("\nTriangle with larger area:")
    area.compare_area()
main()