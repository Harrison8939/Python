#a is a list of numbers,
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []


for number in a:
    if number < 5:
        x.append(number)
        
print(x)