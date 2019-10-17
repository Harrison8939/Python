age = int(input("enter your age\n"))

if age > 17:
    print("can see a rated R movie")

elif age < 17 and age > 12:
    print("Can see a rated PG-13 movie")

else:
    print("can only see Rated PG movies")