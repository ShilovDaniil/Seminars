from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        string += input(f"Enter {i} ") + " "
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")

def change_contact():
    name = input("Введите имя или фамилию контакта: ")
    with open(file_base, encoding="utf-8") as f:
        lines = f.readlines()
    found = False
    for i, line in enumerate(lines):
        if name in line:
            found = True
            new_data = input("Введите новые данные через пробел (фамилия имя отчество номер): ")
            lines[i] = f"{line.split()[0]} {new_data}\n"
            with open(file_base, "w", encoding="utf-8") as f:
                f.writelines(lines)
            print("Данные успешно изменены!")
            break
    if not found:
        print("Контакт не найден.")

def delete_contact():
    name = input("Введите имя или фамилию контакта: ")
    with open(file_base, encoding="utf-8") as f:
        lines = f.readlines()
    found = False
    for i, line in enumerate(lines):
        if name in line:
            found = True
            del lines[i]
            with open(file_base, "w", encoding="utf-8") as f:
                f.writelines(lines)
            print("Контакт успешно удален!")
            break
    if not found:
        print("Контакт не найден.")

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                pass
            case "4":
                change_contact()
            case "5":
                delete_contact()
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()