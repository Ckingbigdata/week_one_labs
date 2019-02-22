'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''

a = int(input("Please input how many miles you need to drive: "))
b = int(input("Please input the MPG of your car: "))
c = int(input("Please input the price per gallon of fuel: "))
d = (a/b) * c

print(f"This trip costs: {d} dollars")


