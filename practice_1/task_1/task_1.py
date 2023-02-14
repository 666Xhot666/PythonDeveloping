# Variant 6
# a*b+21, if a>b
# -5, if a=b
# 3*a/b+1, if a<b
def int_input(name):
    return int(input(f'Enter {name} number'))


def first(a, b):
    return a * b + 21


def second(a, b):
    return -5


def third(a, b):
    return 3 * a / b + 1


__a__ = int_input('first')
__b__ = int_input('second')
if __a__ > __b__:
    print(f'Result :: {first(__a__, __b__)}')
elif __a__ < __b__:
    print(f'Result :: {third(__a__, __b__)}')
else:
    print(f'\tResult :: {second(__a__, __b__)}')
