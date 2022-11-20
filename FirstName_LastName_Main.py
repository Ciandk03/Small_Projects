import Question_1
import Question_2
end = "Y" or "N"
while end == "Y":
    month = str(input("Enter the month:"))
    day = int(input("Enter the day:"))
    Question_1.season(month, day)
    cents = int(input("Enter change due in cents:"))
    Question_2.change(cents)
    end = input('Do you wish to continue? Y/N')
    if end == "N":
        break
    else:
        continue