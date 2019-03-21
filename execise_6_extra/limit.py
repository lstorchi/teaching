limit = int(raw_input("Enter limit value: "))
number = 0
sum = 0

while (True):
    
    if sum > limit:
        break

    number = number + 1
    sum = sum + number 

print number, " and sum ", sum
