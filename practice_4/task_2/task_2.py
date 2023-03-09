def background_color_template_by_num(num):
    background_color_map_raw256 = {
        0: f'\033[38;5;000m\033[48;5;220m {num} \033[0;0m',
        1: f'\033[38;5;000m\033[48;5;222m {num} \033[0;0m',
        2: f'\033[38;5;000m\033[48;5;222m {num} \033[0;0m',
        3: f'\033[38;5;000m\033[48;5;15m {num} \033[0;0m',
        4: f'\033[38;5;000m\033[48;5;15m {num} \033[0;0m',
        5: f'\033[38;5;000m\033[48;5;51m {num} \033[0;0m',
        6: f'\033[38;5;000m\033[48;5;38m {num} \033[0;0m',
        7: f'\033[38;5;000m\033[48;5;39m {num} \033[0;0m',
    }
    key = num
    if key > background_color_map_raw256.__len__()-1:
        key -= background_color_map_raw256.__len__()
    return background_color_map_raw256[key]


def matrix_initialization(length):
    matrix = []
    while matrix.__len__() < length:
        temp_key_row = matrix.__len__()
        matrix.append([])
        temp_key_line = 0
        while temp_key_line < temp_key_row:
            matrix[temp_key_row].append(0)
            temp_key_line = matrix[temp_key_row].__len__()
        while temp_key_line < length:
            matrix[temp_key_row].append(length - temp_key_line + temp_key_row)
            temp_key_line = matrix[temp_key_row].__len__()
    return matrix


def matrix_print(matrix, color_template):
    for row in matrix:
        line = ''
        for element in row:
            line += color_template(element)
        print(f'{line}')


def task_2():
    matrix = matrix_initialization(7)
    matrix_print(matrix, background_color_template_by_num)


if __name__ == "__main__":
    task_2()
