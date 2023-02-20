import sys
import time

from create_func import fcs_gen, birth_gen, gender_gen, fcs_gen_f_100
from sql_query import create_table_request, insert_new_line_request, get_output_from_table_full_name_with_date_of_birth, \
    get_output_from_table_fcs_date_of_birth_gender_full_years, create_index, drop_index, result_selection
from config import cursor, connection


def _1():
    cursor.execute(create_table_request)
    connection.commit()
    print('=' * 20, "Новая таблица создана", '=' * 20, sep='\n')


def _2(full_name, date_of_birth, gender):
    cursor.execute(insert_new_line_request, (full_name, date_of_birth, gender))
    connection.commit()
    print('=' * 20, "Добавлена новая запись", '=' * 20, sep='\n')


def _3_1():
    cursor.execute(get_output_from_table_full_name_with_date_of_birth)
    for _ in cursor:
        print(*_)
    connection.commit()
    print('=' * 20, "Вывод всех строк с уникальным значением ФИО+дата, отсортированным по ФИО", '=' * 20, sep='\n')


def _3_2():
    cursor.execute(get_output_from_table_fcs_date_of_birth_gender_full_years)
    for _ in cursor:
        print(*_)
    connection.commit()
    print('=' * 20, "Вывод ФИО, Дата рождения, пол, кол-во полных лет", '=' * 20, sep='\n')


def _4_1():
    for _ in range(10**6):
        cursor.execute(insert_new_line_request, (fcs_gen(), birth_gen(), gender_gen()))
        connection.commit()
    print('=' * 20, "Добавлены миллион новых записей", '=' * 20, sep='\n')

def _4_2():
    for _ in range(100):
        cursor.execute(insert_new_line_request, (fcs_gen_f_100(), birth_gen(), 'M'))
        connection.commit()
    print('=' * 20, "Добавлены 100 строк, в которых пол мужской и ФИО начинается с 'F'", '=' * 20, sep='\n')


def _5():
    time_request = 0
    for _ in range(5):
        start_time = time.monotonic()
        cursor.execute(result_selection)
        time_request += time.monotonic() - start_time
    time_avg = time_request / 5
    print('=' * 20, f"Время выполнения выборки из таблицы по критерию: пол мужской, ФИО начинается с 'F' = {time_avg}",
          '=' * 20, sep='\n')


def _6():
    time_request_without_idx = 0
    for _ in range(5):
        start_time = time.monotonic()
        cursor.execute(result_selection)
        time_request_without_idx += time.monotonic() - start_time
    time_avg_without_idx = time_request_without_idx / 5
    print(time_avg_without_idx)
    cursor.execute(create_index)
    time_request_with_idx = 0
    for _ in range(5):
        start_time = time.monotonic()
        cursor.execute(result_selection)
        time_request_with_idx += time.monotonic() - start_time
    time_avg_with_idx = time_request_with_idx / 5
    print(time_avg_with_idx)
    print("%.2f" % (100 - (time_avg_with_idx * 100 / time_avg_without_idx)), '%')
    cursor.execute(drop_index)


if __name__ == '__main__':
    args = sys.argv
    globals()[args[1]](*args[2:])