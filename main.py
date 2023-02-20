from practice_3.task_1.task_1 import task_1
from practice_3.task_2.task_2 import task_2


def print_menu():
    print('Select task script for executing >>')
    print('1 -- Task 1')
    print('2 -- Task 2')
    print('3 -- Exit')


# task_1()
# task_2()


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice:'))
        except:
            print('Wrong input. Please enter a number')
        if option == 1:
            task_1()
        elif option == 2:
            task_2()
        elif option == 3:
            print('Thanks for reviewing.')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3')
