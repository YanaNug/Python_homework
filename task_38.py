# доделать телефонный справочник с внешним хранилищем информации, дополнить функционалом добавления информации, удаления и редактирования.
import json
import os


def menu(): 
    print('Меню: ',
          '0 - выход из программы',
          '1 - сохранить',
          '2 - загрузить данные из удаленного хранилища',
          '3 - вывести все контакты',
          '4 - вывести все данные',
          '5 - поиск информации по ФИО',
          '6 - создать контакт',
          '7 - удалить контакт',
          '8 - редактировать контакт',
          '9 - добавить контактые данные', sep='\n')

def choose_data_type():
    type_data = None
    flag = True
    while flag:
        print('Выбирете какие данные добавить: ', '1 - mobilephone', '2 - phone2', '3 - email', '4 - birthday', sep='\n')
        type_data = input('Выбирете цифру: ')
        match type_data:
            case '1':
                type_data = 'mobilephone'
                flag = False
            case '2':
                type_data = 'phone2'
                flag = False
            case '3':
                type_data = 'email'
                flag = False
            case '4':
                type_data = 'birthday'
                flag = False
            case _: flag = True
    return type_data


def save(phone_book):
    os.system('cls||clear')
    with open('phone_book.json', 'w', encoding='utf-8') as pb:
        pb.write(json.dumps(phone_book, ensure_ascii=False, indent=4))
    print('\nТелефонная книга успешно сохранена в удаленное хранилище\n')


def load(): 
    os.system('cls||clear')
    with open('phone_book.json', 'r', encoding='utf-8') as pb: pb_local = json.load(pb)
    print('\nТелефонная книга успешно загружена\n')
    return pb_local



def print_all_fullname(): 
    os.system('cls||clear')
    pb_local = load()
    print("Список контактов:")
    [print(' ', k) for k in pb_local.keys()]
    print()

def print_book(phone_book):
    print() 
    for k,v in phone_book.items():
        print (k," - ", end = " | ")
        for i,j in v.items():
            print (i, j, end = " | ")
        print()
    print() 


def print_all_data_contact(): 
    pb_local = load()
    print_all_fullname()
    f_name = pb_local.get(input("Введите ФИО для поиска всех данных: ").strip(), None)
    if f_name != None:
        for k, v in f_name.items():
            if type(v) == list:
                for i in range(len(v)):
                    print(k, v[i], sep=' ', end='\n')
            else:
                print(k, v)
    else:
        print('\nТакого контакта нет')
    print()


def create_new_contant(): 
    pb_local = load()
    print_all_fullname()
    print('Введите ФИО нового контакта')
    f_name = input("Введите ФИО: ").strip()
    if f_name in pb_local:
        return print("\033[31m {} \033[0m" .format('\nТакой контакт существует. Выбирете пункт 9 в меню - добавить контактые данные\n'))

    type_data = choose_data_type()

    inp_data = input("Введите данные: ")
    pb_local.update({f_name: {'mobilephone': [], 'phone2': [], 'email': [], 'birthday': []}})
    pb_local[f_name][type_data].append(inp_data)
        
    save(pb_local)
    print('Данные добавлены\n')


def delete_contact():
    pb_local = load()
    print_all_fullname()

    print('\nВвод ФИО')
    f_name = input("Введите ФИО, контака который вы хотите удалить: ").lower().strip()
    answer = pb_local.get(f_name, None)
    if answer != None:
        pb_local.pop(f_name)
        save(pb_local)
        print('Контакт удалён.\n')
    else: print('\nТакого контакта нет\n')


def edit_contact():
    pb_local = load()
    print_all_fullname()

    f_name = input("Введите ФИО контакта: ").lower().strip()
    answer = pb_local.get(f_name, None)
    if answer != None:
        count = 0
        dict_res = {}
        print('\nДанные доступные для изменения: ')
        for k, v in pb_local[f_name].items():
            if len(v) > 0:
                for i in v:
                    dict_res[count] = [k, i]
                    print(count, k, i)
                    count += 1         
            else:
                dict_res[count] = [k, v]
                print(count, k, v)
                count += 1

        type_data = None
        flag = True
        while flag:
            type_data = int(input('Выбирете цифру (0, 1, 2 ...). Данные, которые хотите изменить: '))
            if dict_res.get(type_data, 0) != 0:
                try: position = pb_local[f_name][dict_res[type_data][0]].index(dict_res[type_data][1])
                except: position = -1

                if position >= 0: pb_local[f_name][dict_res[type_data][0]][position] = input('Введите новые данные: ')
                else: pb_local[f_name][dict_res[type_data][0]] = [(input('Введите новые данные: '))]

                flag = False
            
        save(pb_local)
        print('Контакт отредактирован\n')
    else: print('\nТакого контакта нет\n')


def add_data():
    pb_local = load()
    print_all_fullname()

    f_name = input("В какой контакт вы хотите добавить данные: ").lower().strip()   
    type_data = choose_data_type()
    inp_data = input("Введите данные для добавления: ")
    if type(pb_local[f_name][type_data]) == list: pb_local[f_name][type_data].append(inp_data)
    else: pb_local[f_name][type_data] = inp_data
        
    save(pb_local)
    print('\nНовые данные добавлены\nТелефонная книга успешно сохранена\n')


try:
    phone_book = load()
except:
    phone_book = {
        "Капарова Марина Романовна": {"mobilephone": ["89035562485", "89053236554"], "birthday": ["17-08-1999"], "email": ["maryy@yandex.ru"]},
        "Пак Вадим Леонидович": {"mobilephone": ["89612252255"], "birthday": ["13-06-1993"], "email": ["yami@yandex.ru"]}}
    save(phone_book)
    print("Телефонная книга не найдена. Создана тестовая версия.\n")

choice = None
while choice != 0:
    menu()
    choice = int(input("Введите пункт меню (цифру): "))
    match choice:
        case 0: print('\nДо свидания!')
        case 1: save(phone_book)
        case 2: load()
        case 3: print_all_fullname()           
        case 4: print_book(phone_book)
        case 5: print_all_data_contact()
        case 6: create_new_contant()
        case 7: delete_contact()
        case 8: edit_contact()
        case 9: add_data()
        case _: print("\nВыбирете пункт меню или выйдите из программы (Цифра: 0)\n")