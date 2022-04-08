#Name: Min Jung
#Due Date: 11/30/2021
#Homework Assignment on Classes and Objects: Lab 2

class VendingMachine:
    def __init__(self, numOfDrinks, numOfBottles, inventory):
        self.numOfDrinks = numOfDrinks
        self.numOfBottles = numOfBottles
        self.inventory = inventory
        
purchase_num_drinks = int(input())
restock_num_bottles = int(input())
result_inventory = 20 - purchase_num_drinks + restock_num_bottles

vendingMachine = VendingMachine(purchase_num_drinks, restock_num_bottles , result_inventory)

print(f'Inventory: {vendingMachine.inventory} bottles')