#stores a value in the variables num, check, which the user inputs
num = int(input("Give me a number to check: "))
check = int(input("Give me a number to divide by: "))


#if statements that test if the number is a multiple of 4
if num % 4 == 0:
    print(num, "Is a multiple of 4")

#if not, test if its an even number
elif num % 2 == 0:
    print(num, "Is an even number")

#else, test if it's an odd number
else:
    print(num, "Is an odd number")

#test the value of check against num, to see if the number divides evenly by check
if num % check == 0:
    print(num, "divides evenly by", check)

#if not even, the string is returned as the below 
else:
    print (num, "does not divide evenly by", check)