numberList = [12,23,55,67,77,89,12,11,23,44]

for number in numberList:
    remainder = number % 3
    if remainder == 0:
        print("The number",number,"is divisible by 3")
    else:
        print("The number",number,"is not divisible by 3")

#start from 5. keep adding 3 to the previous value until it is less than 14
someRange = range(2,21,2)

for given in someRange:
    print(given)


