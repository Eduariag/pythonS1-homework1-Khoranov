#Дополнить телефонный справочник возможностью изменения и удаления данных. 
#Пользователь также может ввести имя или фамилию, и
# Вы должны реализовать функционал для изменения и удаления данных

def delete_person(name):
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)
def change_person(new_name, old_name):
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")
while True:
    mode = input('directory mode' + '\n'
                  +'0-search, 1-read, 2-add, 3-delete, 4-change, 5-enter: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('Whom delete?: ')
        delete_person(name)
    elif mode == '4':
        old_name = input('Whom change?: ')
        new_name = input('New name: ')
        change_person(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('No mode')