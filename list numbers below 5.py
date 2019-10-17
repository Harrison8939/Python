a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
ask = int(input("Enter a number to test which numbers in the list are lower "))

for number in a:
    if number < ask:
        x.append(number)
        
print(x)