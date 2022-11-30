LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def Birthday_Lookup():
    birthdays = {}

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)


def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit a program')

    choice = int(input('Enter your choice: '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter your choice: '))

    return choice


def add(birthdays):
    name = input('Enter a name: ')
    bday = input('Enter a birthday: ')

    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('That entry already exists.')


def look_up(birthdays):
    name = input('Enter a name: ')
    print(birthdays.get(name, 'Not found.'))


def change(birthdays):
    name = input('Enter a name: ')
    if name in birthdays:
        bday = input('Enter a birthday: ')
        birthdays[name] = bday

    else:
        print('That name is not found.')


def delete(birthdays):
    name = input('Enter a name: ')
    if name in birthdays:
        del birthdays[name]
    else:
        print('That name is not found.')


if __name__ == '__main__':
    Birthday_Lookup()
