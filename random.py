import math
cents = int(input("o:"))
def change(cents):
    if cents > 0:
        if cents >= 25:
            change1 = math.floor(cents / 25)
            change = cents - (change1 * 25)
            if change == 0:
                if change1 == 1:
                    print(change1, "Quarter")
                elif change1 >= 2:
                    print(change1, "Qaurters")
            if change1 == 1:
                print(change1, "Quarter")
            elif change1 >= 2:
                print(change1, "Qaurters")
            change2 = math.floor(change / 10)
            change = change - (change2 * 10)
            if change == 0:
                if change2 == 1:
                    print(change2, "Dime")
                elif change2 >= 2:
                    print(change2, "Dimes")
            if change2 == 1:
                print(change2, "Dime")
            elif change2 >= 2:
                print(change2, "Dimes")
            change3 = math.floor(change / 5)
            change = change - (change3 * 5)
            if change == 0:
                if change3 == 1:
                    print(change3, "Nickle")
                elif change3 >= 2:
                    print(change3, "Nickles")
            if change3 == 1:
                print(change3, "Nickle")
            elif change3 >= 2:
                print(change3, "Nickles")
            change4 = math.floor(change / 1)
            if change4 == 1:
                print(change4, "Penny")
            elif change4 >= 2:
                print(change4, "Pennies")
change(cents)