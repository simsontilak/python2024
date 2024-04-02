def main():
    number = int(input("Enter a number: "))
    result = 0
    for i in range(1, number + 1):
        result = result + i
    print("The sum of the numbers:", result)


if __name__ == "__main__":
    main()
