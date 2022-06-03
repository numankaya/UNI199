number = int(input("Enter a ball number: "))
if number < 0 or number > 100:
    print("Invalid ball number.")
else:
    if number == 2 or number % 2 == 1:
        if 0 <= number <= 24:
            print("The ball is green")
        elif 25 <= number <= 74:
            print("The ball is red")
        elif 75 <= number <= 100:
            print("The ball is yellow")
    elif number != 2 and number % 2 == 0:
        if 0 <= number <= 73 and number % 6 == 0:
            print("The ball is blue")
        elif 74 <= number <= 100 and number % 3 == 0:
            print("The ball is orange")
        else:
            print("The ball is white")