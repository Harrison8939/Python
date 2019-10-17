#a is a list, x is an empty list, and ask is an input variable
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
ask = int(input("Enter a number to test which numbers in the list are lower "))

#tests each number in list a, then if the current number is below input, appends it to empty list x
for number in a:
    if number < ask:
        x.append(number)

#prints numbers from loop that were stored in x
print(x)