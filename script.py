import os
import shutil


class Utils:
    def get_clean_screen(self):
        if shutil.which('cls') is not None:
            return "cls"
        elif shutil.which('clear') is not None:
            return "clear"
        else:
            print("Clean screen command not found. Please check 'get_clean_screen' function.")
            return

class Functions:
    util = Utils()
    def arithmetic(self, operation):
        num1 = float(input('Enter a number: '))
        num2 = float(input('Enter another number: '))
        if operation == 'add':
            result = num1 + num2
            input("Press any key to continue...")
            os.system(util.get_clean_screen())
        elif operation == 'subtract':
            result = num1 - num2
            input("Press any key to continue...")
            os.system(util.get_clean_screen())
        elif operation == 'multiply':
            result = num1 * num2
            input("Press any key to continue...")
            os.system(util.get_clean_screen())
        elif operation == 'divide':
            if num2 == 0:
                print("Cannot divide by 0.")
                input("Press any key to continue...")
                os.system(util.get_clean_screen())
                return
            result = num1 / num2
        else:
            print('Invalid operation.')
            return
        if result.is_integer():
            result = int(result)
            input("Press any key to continue...")
            os.system(util.get_clean_screen())
        print(num1, operation, num2)
        if result == 13:
            print('The more you suck it, the more it grows')
            input("Press any key to continue...")
            os.system(util.get_clean_screen())
        elif result == 11:
            print('Suck it then')
            input("Press any key to continue...")
            os.system(util.get_clean_screen())
        else:
            print(f'The result is: {result}')
            input("Press any key to continue...")
            os.system(util.get_clean_screen())

    def table(self, num):
        for i in range(13):
            print(f"{num} x {i} = {num * i}")
            input("Press any key to continue...")
            os.system(util.get_clean_screen())

def use_menu():
    util = Utils()
    func = Functions()
    os.system(util.get_clean_screen())
    menu = True
    while menu:
        print('1) Addition')
        print('2) Subtraction')
        print('3) Multiplication')
        print('4) Division')
        print('5) Tables')
        print('6) Exit')
        option = input('What operation do you want to perform?: ')
        if option == '1':
            func.arithmetic('add')
        elif option == '2':
            func.arithmetic('subtract')
        elif option == '3':
            func.arithmetic('multiply')
        elif option == '4':
            func.arithmetic('divide')
        elif option == '5':
            num = int(input('Enter a number: '))
            func.table(num)
        elif option == '6':
            print('Closing program... \n~CHUPA productions~')
            quit()
        else:
            print('Invalid response. Trying again...')
util = Utils()
follow = True
while follow:
    os.system(util.get_clean_screen())
    keep = input('Do you want to start? (y/n) > ')
    keep = keep.lower()
    if keep == 'y':
        use_menu()
    elif keep == 'n':
        follow = False
        print('Closing program... \n~CHUPA productions~')
        quit()
    else:
        print('Invalid response. Trying again... ')
