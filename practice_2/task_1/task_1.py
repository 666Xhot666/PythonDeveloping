# Variant 6
from math import sin


def int_input(name):
    return int(input(f'Enter {name} :\t'))


def sin_based_function(a, b):
    return sin(a + b) * sin(a - b)


def first_task():
    print(f'Result :: {sin_based_function(a=int_input("alfa"),b=int_input("beta"))}')


def sportsman_function(m, k, checkpoint):
    if m <= 0 or k <= 0:
        return 'Never'
    days = 1
    while checkpoint > m:
        checkpoint -= m * k
        days += 1
    return days


def second_task():
    checkpoint = 50
    m, k = int_input('distance of first day (km)'), int_input('percentage of distance increase')/100
    print(f'The athlete will run more than {checkpoint} km in {sportsman_function(m, k, checkpoint)} days')


if __name__ == "__main__":
    print('....\nRun first task ::>\n')
    first_task()
    print('....\nRun second task ::>\n')
    second_task()
