from database.database import open_data, save_data
from handler.classRoom import create_class_room, add_new_student


def output_menu_item():
    print('0 - завершить работу программы.')
    print('1 - добавить новый класс.')
    print('2 - список классов.')
    print('3 - вывести информацию об ученике.')
    print('4 - добавить нового ученика.')
    print('5 - применить изменения.')


def main():
    content = open_data()

    print('Добро пожаловать, Пользователь!')
    print('Для продолжения введите одну из команд. \n')

    while True:
        output_menu_item()
        user_input_command = input('Введите команду: ')

        if user_input_command == '0':
            break
        elif user_input_command == '1':
            new_class_room = create_class_room()

            content[new_class_room] = {
                'students': {}
            }
        elif user_input_command == '2':
            for classroom in content:
                print(f'Класс: {classroom}')

                for student in content[classroom]['students']:
                    print(student)

                print()
        elif user_input_command == '3':
            student_name, classroom_name = input('Введите имя ученика и название класса через запятую: ').split(',')

            print(
                content[classroom_name]['students'][student_name]
            )
        elif user_input_command == '4':
            input_class_room = input('Введите название класса: ')

            if input_class_room in content:
                student_name = add_new_student()
                content[input_class_room]['students'][student_name] = {}
            else:
                print('Ошибка! Такого класса не существует.')
        elif user_input_command == '5':
            save_data(content)


if __name__ == '__main__':
    main()
