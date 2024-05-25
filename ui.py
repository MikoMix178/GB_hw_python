from logger import input_data, print_data, remove_data, edit_data


def interface():
    print("Добрый день! Это справочник по заданию от GeekBrains! \n 1 - запись данных \n 2 - вывод данных \n 3 - удаление данных \n 4 - изменить данные \n 0 - выход" )
    command = int(input('Введите число: '))
    
    while command != 0:
        if command == 1:
            input_data()
        elif command == 2:
            print_data()
        elif command == 3:
            remove_data()
        elif command == 4:
            edit_data()
        else:
            print('Неправильный ввод')
        command = int(input('Введите число: '))
        
    