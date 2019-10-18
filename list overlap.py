#Original list below
 
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



#Generates two lists full of random numbers (a,b) (c) is an empty list.
import random
a = list(random.sample(range(30), 10 + random.randrange(4)))
b = list(random.sample(range(40), 10 + random.randrange(6)))
c = []

#Prints random numbers just to check it works
print(a)
print(b)

#Loop that tests each number in b against each number in a, appends non duplicates to c
for number in b:
    if number in a:
        if number not in c:
            c.append(number)

print (c)
        