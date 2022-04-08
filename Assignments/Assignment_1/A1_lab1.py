#Name: Min Jung
#Due Date: September 13, 2021 till 10pm

total_change = int(input("Total Change Amount: "))

if total_change <= 0:
    print("No change")

dollar = int(total_change/100)
total_change = total_change - (dollar *100)

quarter = int(total_change/25)
total_change = total_change - (quarter *25)

dime = int(total_change/10)
total_change = total_change - (dime *10)

nickel = int(total_change/5)
total_change = total_change - (nickel *5)

penny = int(total_change/1)
total_change = total_change - (penny *1)


if dollar == 1:
    print('1 Dollar')
elif dollar > 1:
    print(dollar, 'Dollars')

if quarter > 1:
    print(quarter, 'Quarters')
elif quarter == 1:
    print('1 Quarter')

if dime > 1:
    print(dime, 'Dimes')
elif dime == 1:
    print('1 Dime')
    
if nickel > 1:
    print(nickel, 'Nickels')
elif nickel == 1:
    print('1 Nickel')

if penny > 1:
    print(penny, 'Pennies')
elif penny == 1:
    print('1 Penny')
    