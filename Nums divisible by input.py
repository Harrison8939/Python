#number to divide by is stored in variable num
num = int(input("Please choose a number to divide"))

#creates a list of numbers from 1 to the chosen input number
listRange = list(range(1,num+1))

#an empty list
divisorList = []

#takes each number in the listRange, and tests the modulus of it against input num
#appends each number in the list to divisorList that returns a modulus of 0
for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)