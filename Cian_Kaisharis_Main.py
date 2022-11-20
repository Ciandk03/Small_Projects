#I certify that the code in this Python file, is entirely my own work.
import Question_1
import Question_2
end = "Y" or "N"
while end == "Y":
    month = input("Enter the month:")
    day = int(input("Enter the day:"))
    Question_1.season(month, day)
    cents = int(input("Enter change due in cents:"))
    Question_2.change(cents)
    end = input('Do you wish to continue? Y/N:')
    end = end.upper()
    if end == "N":
        break
    else:
        continue