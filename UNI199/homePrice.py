price = 90000
number_of_rooms = int(input("Enter the number of rooms: "))
if number_of_rooms<1:
    print("Houses in Scranton have minimum 1 room.")
price = price + (number_of_rooms-1)*10000
print(price)

distance = int(input("Enter the distance from city center:"))
if distance<0 and distance>30:
    print("The distance is out of range.")
price = price - (distance*200)
print(price)

garden = int(input("Enter the area of the garden (m^2):"))
if garden<0 or garden>20:
    print("The area is out of range.")
elif garden<=10:
    price = price + 5000
elif 10<garden<=20:
    price = price + 5000 + 700*(garden-10)
print(price)