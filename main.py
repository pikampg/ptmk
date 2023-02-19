import datetime

import psycopg2
from config import host, user, password, db_name, connection
from create_func import create_table, insert_new_line, full_output
from create_func import get_output_full_name_with_date_of_birth
from create_func import get_output_fcs_date_of_birth_gender_full_years
from create_func import fcs_gen, gender_gen, birth_gen
from create_func import input_mln, input_gender_m_f_100, time_selection

connection = None

try:
    connection = psycopg2.connect(
        database=db_name,
        host=host,
        user=user,
        password=password
    )
    # create_table()                                                        # myAPP 1
    # insert_new_line(fcs_gen(), birth_gen(), gender_gen())                 # myAPP 2
    # get_output_full_name_with_date_of_birth()                             # myAPP 3.1
    # get_output_fcs_date_of_birth_gender_full_years()                      # myAPP 3.2
    # full_output()
    # input_mln(fcs_gen(), birth_gen(), gender_gen())                       # myAPP 4.1
    # input_gender_m_f_100()                                                # myAPP 4.2
    time_selection()

except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')