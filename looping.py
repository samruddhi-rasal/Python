marks = 45
if marks >= 90:
    print("Grade A+")
    if marks >= 95:
        print("Outstanding")
        print("Keep it up! Great work")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

#switch case 
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
            print("Tuesday")
    case 3:
            print("Wednesday")
    case 4:
            print("Thrusday")
    case 5:
            print("Friday")
    case 6:
            print("Saturday")
    case 7:
            print("Sunday")
    case _:
            print("Invalid day")



