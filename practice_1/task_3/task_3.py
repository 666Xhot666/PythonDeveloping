# Variant 6
def int_input():
    num = int(input('Enter number <<N>> 1<=N>=9:\t'))
    if num < 1 or num > 9:
        print('You have entered wrong number, try again')
        return int_input()
    return num


def print_strange_picture(psp_num):
    c_index = 1

    # Creating and formatting each line of picture
    def get_line(gt_num):
        line = []
        while gt_num >= 1:
            line.append(str(gt_num))
            gt_num -= 1
        return ' '.join(line)

    while c_index <= psp_num:
        print(f'{get_line(c_index)}')
        c_index += 1


print_strange_picture(int_input())
