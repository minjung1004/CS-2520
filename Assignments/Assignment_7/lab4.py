#Name: Min Jung
#Due Date: 11/30/2021
#Homework Assignment on Classes and Objects: Lab 4

#Implement a class Worker to handle weekly worker’s pay (including overtime pay). 

class Worker:
    def __init__(self, hours, pay_rate, base_hour = 40, overtime_multi = 1.5):
        self.hours = hours
        self.pay_rate = pay_rate
        self.base_hour = base_hour
        self.overtime_multi = overtime_multi
    def gross_pay(self):
        if self.hours > self.base_hour:
            self.overtime_hours =  self.hours - self.base_hour
            self.overtime_pay = self.overtime_hours * self.pay_rate + self.overtime_multi
            self.gross_pay = self.base_hour * self.pay_rate + self.overtime_pay
            print(f'Gross pay + Overtime: ${self.gross_pay:.2f}')
        else:
            self.gross_pay = self.hours * self.pay_rate
            print(f'Gross pay: ${self.gross_pay:.2f}')
def main():
    hours = float(input("Enter the number of hours worked: "))
    pay_rate= float(input("Enter the hourly pay rate: "))
    total = Worker(hours, pay_rate)
    total.gross_pay()        
main()      