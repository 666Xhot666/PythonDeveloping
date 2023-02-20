import sys


def string_input():
    string_for_cutting = input('Enter string for cutting (length of string should be more than 21)\n')
    if string_for_cutting.__len__() <= 21:
        sys.exit('String length is shorter than 21 elements. We can`t cut anything.')
    return string_for_cutting


def cutting(string_for_cutting, start=18, end=-3):
    return string_for_cutting[start:end]


def task_1():
    string_for_cutting = string_input()
    print('\033[33m\033[1m'+'Result of cutting'+'\033[0m')
    print(f'{cutting(string_for_cutting)}')

if __name__ == '__main__':
    task_1()