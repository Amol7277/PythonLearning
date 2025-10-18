#match the days
Day = float(input("Enter the Day: ").strip())

match Day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case 1.5:
        print("Friday")
    case _:
        print("Invalid Day")
        
