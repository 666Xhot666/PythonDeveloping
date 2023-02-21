import re


def string_input():
    try:
        word = input('Enter word for calculating:\n').strip()
        word = re.match(r'^\w+?[A-Za-z]+\S+\d?', word).group(0)
    except:
        print('Wrong input. Please try again')
        string_input()
    return word


def calculate_ascii_sum(word):
    word_sum = 0
    for char in word:
        word_sum += ord(char)
    return word_sum


def task_2():
    word = string_input()
    print('Result ::\nSum of ASCII codes are ::: ')
    print(f'\033[33m{calculate_ascii_sum(word)}\033[0m\n')


if __name__ == '__main__':
    task_2()
