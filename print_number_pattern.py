def print_pattern(a_number):
    result = ''
    for number in range(1, a_number + 1):
        result = result + str(number) + ' '
    return result


def main():
    for number in range(1, 6):
        print(print_pattern(number))


if __name__ == '__main__':
    main()
