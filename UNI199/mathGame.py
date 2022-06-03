import random
operation = int(input("Enter operation type (1-summation; 2-multiplication):"))
while operation != 1 and operation != 2:
    print("Invalid number!\n")
    operation = int(input("Enter operation type (1-summation; 2-multiplication):"))

num_cor = 0
num_que = 0
continu = 1
while continu == 1:
    num_que += 1
    a = int(input("Enter the lower limit:"))
    b = int(input("Enter the upper limit:"))

    while a > b or a < 1 or b > 100:
        print("invalid:")
        a = int(input("Enter the lower limit:"))
        b = int(input("Enter the upper limit:"))



    random_1 = random.randint(a, b)
    random_2 = random.randint(a, b)
    result = 0

    operator = ""
    if operation == 1:
        operator = "+"
        result = random_1 + random_2
    else:
        operator = "x"
        result = random_1 * random_2

    print("What is ", random_1, operator, random_2, "\n")
    answer = int(input("Your answer: = "))
    if answer != result:
        print(random.choice(["Well, not really...", "Sorry that is wrong...", "Ughh... not quite right."]))
    else:
        print(random.choice(["Congratulations!", "Well done!", "That’s right!"]))
        num_cor += 1
    continu = int(input("Continue? (1-yes; any other number-no):"))

print("You answered {} % of the questions correctly.".format(num_cor / num_que))
