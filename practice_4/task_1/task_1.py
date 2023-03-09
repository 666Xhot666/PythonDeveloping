def array_input():
    number_array = []
    print('Enter array ::')
    while True:
        try:
            temp_number = int(input(f'Enter {number_array.__len__()+1} member of array, for finish press Enter:\n'))
            number_array.append(temp_number)
        except:
            print(f"Yours current array are: \n {number_array}")
            print('You are really want to finish typing the array? ')
            temp = input('Press '+'\033[33m\033[1m'+'Y'+'\033[0m'+' for finish :: \t')
            if temp == "Y" or temp == "y":
                return number_array


def calculation_function(num_array):
    result = 0
    if num_array.__len__() < 1:
        return 0
    for num in num_array:
        if num > 0 and num % 2:
            result += num
    return result


def task_1():
    print(f'\n Result of array calculation : \t {calculation_function(array_input())}\n')


if __name__ == '__main__':
    array_input()

