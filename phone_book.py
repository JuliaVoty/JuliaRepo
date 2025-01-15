import time


def search(phone_book):
    name = input('Введите имя для поиска: ')
    if name in phone_book:
        print(f'Контакт {name}, номер телефона {phone_book[name]}')
    else:
        print('Контакт не найден')


def add_contact(phone_book):
    name = input('Введите имя: ')
    number = input('Введите номер телефона: ')
    if name in phone_book:
        print('Контакт с таким именем уже существует')
    else:
        phone_book[name] = number
        print(f'Контакт {name} добавлен')


def del_contact(phone_book):
    name = input('Введите контакт, который хотите удалить: ')
    if name in phone_book:
        del phone_book[name]
        print(f'Контакт {name} удалён')
    else:
        print('Контакт не найден')


def show_contacts(phone_book):
    for key in phone_book:
        print(f'Имя: {key}, Номер телефона: {phone_book.get(key)}')


def ring(phone_book):
    contact = input("Введите имя кому вы хотите позвонить: ")
    if contact in phone_book:
        print(f"Набираю номер {phone_book.get(contact)} ...")
        time.sleep(2)
        for x in range(2):
            print("ring.... ring....")
            time.sleep(2)
        print("Абонент не отвечает... Я думаю это потому что у нас не вэб версия, а Beta")
    else:
        print("К сожалению, такого контакта нет в записной книге")


def sub_menu():
    action = input("1. Добавить контакт\n2. Удалить контакт\n 3.Вернуться в меню\n")
    match action.split():
        case["1"]:
            add_contact(phone_book)
        case["2"]:
            del_contact(phone_book)
        case["3"]:
            print("")

phone_book = {}
action = ''

while action != 'Выход':
    action = input('Меню:\n1. Поиск\n2. Изменение контактов\n3. Показать контакты\n4. Позвонить (beta 2.0)\n'
                   'Введите "Выход" для завершения\n')
    match action.split():
        case['1']:
            search(phone_book)
        case['2']:
            sub_menu()
        case['3']:
            show_contacts(phone_book)
        case['4']:
            ring(phone_book)








