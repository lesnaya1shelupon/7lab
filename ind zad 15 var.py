import sys
from datetime import datetime, timedelta
import datetime

if __name__ == '__main__':
    spisok = []
    new_spisok = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            surname = input("Фамилия: ")
            name = input("Имя: ")
            post = input("знак Зодиака: ")
            day, month, year = input("Дата рождения: ").split(" ")
            datas = f'{year} {month} {day}'
            spisok_new = {
                'surname': surname,
                'name': name,
                'post': post,
                'data': datas,
            }

            spisok.append(spisok_new)

            if len(spisok) > 1:
                spisok.sort(key=lambda item: item.get('data', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 15,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^15} | {:^30} | {:^20} | {:^15} | '.format(
                    "№",
                    "Дата рождения",
                    "Фамилия",
                    "Имя",
                    "Знак Зодиака"

                )
            )
            print(line)

            # Вывести данные о всех сотрудниках.
            for idx, spisok_new in enumerate(spisok, 1):
                print(
                    '| {:>4} | {:<15} | {:<30} | {:<20} | {:<15} | '.format(
                        idx,
                        spisok_new.get('data', ''),
                        spisok_new.get('surname', ''),
                        spisok_new.get('name', ''),
                        spisok_new.get('post', 0)

                    )
                )

            print(line)
        elif command == 'find':
            find = input("Введите знак Зодиака: ")
            for find_item in spisok:
                if find == find_item['post']:
                    new_spisok.append(find_item)
                # print(find_item)

            if len(new_spisok) > 0:
                line_new = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                    '-' * 4,
                    '-' * 15,
                    '-' * 30,
                    '-' * 20,
                    '-' * 15
                )
                print(line_new)
                print(
                    '| {:^4} | {:^15} | {:^30} | {:^20} | {:^15} | '.format(
                        "№",
                        "Дата рождения",
                        "Фамилия",
                        "Имя",
                        "Знак Зодиака"

                    )
                )
                print(line_new)

                for idx_new, spisok_new_new in enumerate(new_spisok, 1):
                    print(
                        '| {:>4} | {:<15} | {:<30} | {:<20} | {:<15} | '.format(
                            idx_new,
                            spisok_new_new.get('data', ''),
                            spisok_new_new.get('surname', ''),
                            spisok_new_new.get('name', ''),
                            spisok_new_new.get('post', 0)

                        )
                    )

                print(line_new)
            else:
                print('Таких пользователей не найдено', file=sys.stderr)
        elif command == 'help':
            print('Список команд:\n')
            print('add - добавить пользователя.')
            print('list - вывести список пользователей.')
            print('find <Знак зодиака> - запросить пользователей по знаку Зодиака.')
            print('help - Справочник.')
            print('exit - Завершить пработу программы.')
        else:
            print(f'Команда <{command}> не существует.', file=sys.stderr)
            print('Введите <help> для просмотра доступных команд')
