#I certify that the code in this Python file, is entirely my own work.
#cents = int(input("Enter amount of change:"))
Q = 25
D = 10
N = 5
def change(cents):
    quarters = (cents - (cents % Q )) / Q
    Amount1 = cents % Q
    dimes = (Amount1 - (Amount1 % D)) / D
    Amount2 = Amount1 % D
    nickles = (Amount2 -(Amount2 % N)) / N
    pennies = Amount2 % N
    if quarters ==1 :
        print(int(quarters), "Quarter")
    elif quarters >= 2 or quarters == 0:
        print(int(quarters), "Quarters")
    if dimes ==1 :
        print(int(dimes), "Dime")
    elif dimes >= 2 or dimes == 0:
        print(int(dimes), "Dimes")
    if nickles ==1 :
        print(int(nickles), "Nickle")
    elif nickles >= 2 or nickles == 0:
        print(int(nickles), "Nickles")
    if pennies ==1 :
        print(int(pennies), "Penny")
    elif pennies >= 2 or pennies == 0:
        print(int(pennies), "Pennies")
#change(cents)