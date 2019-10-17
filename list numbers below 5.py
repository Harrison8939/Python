#a is a list of numbers, x is an empty list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []

#tests each number in list a, if the number is below 5, appends them to list x
for number in a:
    if number < 5:
        x.append(number)

#prints the new list of numbers below 5
print(x)