numberlist = (1,2,3,4,5,55,99,8,12,15,18,-1,-5,-10)

#function to get highest number returned to highestnum 
def get_highest(numbers,highestnum=0):
    for num in numberlist:
        if num > highestnum:
            highestnum = num
    return highestnum
    

#function to get lowest number returned to lowestnum
def get_lowest(numbers,lowestnum=0):
    for num in numberlist:
        if num < lowestnum:
            lowestnum = num
    return lowestnum

#tests
print (get_highest(numberlist))
print (get_lowest(numberlist))


