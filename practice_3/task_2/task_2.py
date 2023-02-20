import re


def string_input():
    return input('Enter string for filtering:\n')


def find_words(string_for_filtering):
    string_for_filtering_arr = re.split(r'\s|\W\s|\W', string_for_filtering)
    result = []
    for word in string_for_filtering_arr:
        if re.findall(r'e', word).__len__() == 3:
            result.append(word)
    return result


def task_2():
    string_for_filtering = string_input()
    print('\nResult :: \n')
    print(f'{",  ".join(find_words(string_for_filtering))}')


if __name__ == '__main__':
    task_2()
