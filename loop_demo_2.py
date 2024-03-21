# Write a program to print odd numbers starting from the number 7 and ending at the number 91.
# The number 7 and 91 should also be printed.
# Using while loop

index = 91
while index >= 7:
    print(index)
    index -= 2

for index in range(91, 6, -2):
    if index % 3 == 0:
        continue
    else:
        print(index)
    if index == 71:
        break

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for week_day in week_days:
    print(week_day)
