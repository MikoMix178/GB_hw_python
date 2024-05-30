from data_create import name_data, surname_data, phone_data, address_data
import csv

filename = 'data.csv'
def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    with open(filename, 'a+', encoding = 'utf-8', newline='') as f:
        fieldnames = ['name', 'surname','phone','address']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({'name':name, 'surname':surname,'phone':phone,'address':address})

def print_data():
    print("Вывожу данные из файла: \n")
    with open(filename, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'], row['surname'],row['phone'],row['address'])
        
def remove_data():
        a = input('Введите Имя или Фамилию для удаления: ')
        with open(filename, newline='', encoding="utf-8") as csvfile:
            reader = list(csv.DictReader(csvfile))
            for row in reader:
                if row['name'] == a or row['surname'] == a:
                    reader.remove(row)
        with open(filename, 'w', encoding = 'utf-8', newline='') as f:
            fieldnames = ['name', 'surname','phone','address']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(reader)
        print('Данные удалены')
    
def edit_data():
    a = input('Введите Имя или Фамилию для изменения: ')
    with open(filename, newline='', encoding="utf-8") as csvfile:
            reader = list(csv.DictReader(csvfile))
            for row in reader:
                if row['name'] == a:
                    row['name'] = input("Введите новое значение имени: ")
                if row['surname'] == a:
                    row['name'] = input("Введите новое значение фамилии: ")
    with open(filename, 'w', encoding = 'utf-8', newline='') as f:
        fieldnames = ['name', 'surname','phone','address']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)
    print("Замена выполнена успешно")

def copy_to_another():
    str_num = int(input('Введите номер строки для переноса в другой файл: '))
    with open(filename, newline='', encoding="utf-8") as csvfile:
        reader = list(csv.DictReader(csvfile))
        needed_string = reader[str_num]
        reader.remove(needed_string)
    with open(filename, 'w', encoding = 'utf-8', newline='') as f:
        fieldnames = ['name', 'surname','phone','address']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)
    with open('new_file.csv', 'a+', encoding = 'utf-8', newline='') as f:
        fieldnames = ['name', 'surname','phone','address']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(needed_string)
