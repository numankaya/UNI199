weeks = int(input("How many weeks do you work?"))
if weeks <= 0:
    print("Invalid week input!")

weekday_earning = int(input("Enter weekday earnings [$]:"))
if weekday_earning <= 0:
    print("Weekday earnings should be higher than zero!")

weekend_earning = int(input("Enter weekend earnings [$]:"))
if weekend_earning <= weekday_earning:
    print("Weekend earnings should be higher than the weekday earnings!")

grocery = int(input("Enter the cost of groceries[$]:"))
if grocery <= 0:
    print("Grocery expenditure should be positive!")

rent = int(input("Enter the rent[$]:"))
if rent <= 0:
    print("Rent should be positive!")

money = 500
earning = 0
spending = 0

for i in range(1, weeks + 1):
    if i % 2 == 1:  # 1 3 5 7
        for j in range(1, 8):
            earning = 0
            spending = 0
            if j == 1:
                earning = weekday_earning
            elif j == 3:
                earning = weekday_earning
                spending = grocery
            elif j == 5:
                earning = weekday_earning
            elif j == 7:
                earning = weekend_earning
            money = money + earning - spending
            print("Week {} day {} earnings: {} spendings: {} remaining: {}".format(i, j, earning, spending, money))

    elif i % 2 == 0:  # 2 4 6
        for j in range(1, 8):
            earning = 0
            spending = 0
            if j == 2:
                earning = weekday_earning
            elif j == 3:
                spending = grocery
            elif j == 4:
                earning = weekday_earning
            elif j == 6:
                earning = weekend_earning
                if i % 4 == 0:
                    spending = spending + rent

            money = money + earning - spending
            print("Week {} day {} earnings: {} spendings: {} remaining: {}".format(i, j, earning, spending, money))
