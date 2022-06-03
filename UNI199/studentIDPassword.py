def verify_id(id, year, college):
    if (len(str(id)) == 8) and (str(id)[0] == str(year)[-2] and str(id)[1] == str(year)[-1]) and (
            str(id)[2] == str(college)):
        return True
    return False

def verify_pass(year, password):
    if (len(str(password)) == 6) and (str(password)[0] != "0") and (
            str(password)[:2] != str(year)[-2:] and str(password)[-2:] != str(year)[-2:]):
        return True
    return False

students = int(input("Please enter number of students: "))
for i in range(students):
    print("\nStudent # " + str(i + 1))

    year = int(input("Enter the registaration year: "))
    while len(str(year)) != 4:
        print("Year must contain 4 digits")
        year = int(input("Enter the registration year: "))

    college = int(input("Enter college (1: CE, 2: CASE 3: SOM):"))
    while college != 1 and college != 2 and college != 3:
        print("Invalid number")
        college = int(input("Enter college (1: CE, 2: CASE 3: SOM "))

    ID = int(input("Enter student ID: "))
    while verify_id(ID, year, college) == False:
        print("Invalid student ID!")
        ID = int(input("Enter student ID: "))

    password = int(input("Enter password: "))
    while verify_pass(year, password) == False:
        print("Invalid password!")
        password = int(input("Enter password: "))
    print("Your ID and password have been verified")
