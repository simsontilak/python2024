def print_table(times, length):
    for index in range(1,length + 1):
        print(index, "x", times, "=", index * times)


print_table(16, 12)

print("============")

print_table(12, 16)

print("============")

print_table(6, 12)
