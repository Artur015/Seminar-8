from return_data_file import data_file
from rows_numeration import fix_row_numbers

def copy_file():
    print("Выберите файл, в который вы хотите скопировать данные")
    data, nf = data_file()
    print("Выберите файл, из которого вы хотите скопировать данные")
    data_copy, nf_copy = data_file()

    
    count_rows = len(data_copy)
    if count_rows == 0:
        print("Копируемый файл пустой!")
    else:
        
        number_row = int(input(f"Введите номер строки для копирования "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка! "
                                   f"Введите номер строки для копирования "
                                   f"от 1 до {count_rows}: "))

       
        copy_row = data_copy[number_row - 1]
        data.append(copy_row)
        
        
        count_rows_new = len(data)
        
        
        data[-1] = f"{count_rows_new};{';'.join(copy_row.split(';')[1:])}"

        
        delete_copy_row = input("Хотите ли вы удалить скопированную строку из файла? (1-да/2-нет): ").lower()
        
        if delete_copy_row == '1':
            
            del data_copy[number_row - 1]

            with open(f'db/data_{nf_copy}.txt', 'w', encoding='utf-8') as file_copy:
                file_copy.writelines(data_copy)
            
            fix_row_numbers(f'db/data_{nf_copy}.txt')
        
        with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)
        
        
        print(f"Строка скопирована! Новый номер строки: {count_rows_new}")

