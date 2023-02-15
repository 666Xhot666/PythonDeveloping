# Variant 6

def fib_list(n_start, n_end):
    # a => first element of fibonacci list
    # b => second element of fibonacci list
    # index => start index for fibonacci generation loop
    # f_list => result list
    a, b, index, f_list = 0, 1, 2, []
    while index <= n_end:
        f_temp = a + b
        a = b
        b = f_temp
        if index >= n_start:
            f_list.append(f_temp)
        index += 1
    return f_list


start_index, end_index = 5, 25
_f_list = fib_list(start_index, end_index)
print(
    f'Fibonacci list from {start_index} to {end_index} element :: \n\t{_f_list} \n List length :: {_f_list.__len__()}')
