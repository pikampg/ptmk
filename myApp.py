import sys

import time

from create_func import fcs_gen, birth_gen, gender_gen, fcs_gen_f_100
from sql_query import create_table_request, insert_new_line_request, get_output_from_table_full_name_with_date_of_birth, \
    get_output_from_table_fcs_date_of_birth_gender_full_years
from sql_query import result_selection
from config import cursor, connection


def _1():
    cursor.execute(create_table_request)
    connection.commit()


def _2(full_name, date_of_birth, gender):
    cursor.execute(insert_new_line_request, (full_name, date_of_birth, gender))
    connection.commit()


def _3_1():
    cursor.execute(get_output_from_table_full_name_with_date_of_birth)
    for _ in cursor:
        print(*_)
    connection.commit()


def _3_2():
    cursor.execute(get_output_from_table_fcs_date_of_birth_gender_full_years)
    for _ in cursor:
        print(*_)
    connection.commit()


def _4_1():
    for _ in range(10):
        cursor.execute(insert_new_line_request, (fcs_gen(), birth_gen(), gender_gen()))
        connection.commit()


def _4_2():
    for _ in range(10):
        cursor.execute(insert_new_line_request, (fcs_gen_f_100(), birth_gen(), 'M'))
        connection.commit()


def _5():
    start_time = time.monotonic()
    cursor.execute(result_selection)
    print(time.monotonic() - start_time)


if __name__ == '__main__':
    args = sys.argv
    globals()[args[1]](*args[2:])