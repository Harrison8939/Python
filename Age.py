#Store input of age in variable age
age = int(input("enter your age\n"))

#test if age is over 17
if age > 17:
    print("can see a rated R movie")


#test if age is between 17 and 12
elif age < 17 and age > 12:
    print("Can see a rated PG-13 movie")

#only remaining options are if age is under 13, prints this response
else:
    print("can only see Rated PG movies")