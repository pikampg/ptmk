import datetime
import random
import string
import time

from sql_query import create_table_request, insert_new_line_request, full_table
from sql_query import get_output_from_table_full_name_with_date_of_birth, result_selection
from sql_query import get_output_from_table_fcs_date_of_birth_gender_full_years
from config import cursor, connection


def create_table():
    cursor.execute(create_table_request)
    connection.commit()
    return


def insert_new_line(full_name, date_of_birth, gender):
    cursor.execute(insert_new_line_request, (full_name, date_of_birth, gender))
    connection.commit()
    return


def get_output_full_name_with_date_of_birth():
    cursor.execute(get_output_from_table_full_name_with_date_of_birth)
    for _ in cursor:
        print(*_)
    connection.commit()


def get_output_fcs_date_of_birth_gender_full_years():
    cursor.execute(get_output_from_table_fcs_date_of_birth_gender_full_years)
    for _ in cursor:
        print(*_)
    connection.commit()


def full_output():
    cursor.execute(full_table)
    for _ in cursor:
        print(_)
    connection.commit()


def fcs_gen():
    fcs = ''
    for _ in range(3):
        letter = random.choice(string.ascii_letters)
        fcs += letter.upper()
    return fcs


def gender_gen():
    gender = ['M', 'W']
    return random.choice(gender)


def birth_gen():
    year = random.randint(1923, 2023)
    month = random.randint(1, 12)
    day = 0
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month == 2:
        day = random.randint(1, 29)
    elif month == 2:
        day = random.randint(1, 28)
    elif month in (1, 3, 5, 7, 8, 10, 12):
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
    return f'{year}-{month}-{day}'


def fcs_gen_f_100():
    fcs = 'F'
    for _ in range(2):
        letter = random.choice(string.ascii_letters)
        fcs += letter.upper()
    return fcs


def input_mln(full_name, date_of_birth, gender):
    for _ in range(10**7):
        cursor.execute(insert_new_line_request, (fcs_gen(), birth_gen(), gender_gen()))
        connection.commit()
    return


def input_gender_m_f_100():
    for _ in range(100):
        cursor.execute(insert_new_line_request, (fcs_gen_f_100(), birth_gen(), 'M'))
        connection.commit()
    return


def time_selection():
    start_time = time.monotonic()
    cursor.execute(result_selection)
    print(time.monotonic() - start_time)