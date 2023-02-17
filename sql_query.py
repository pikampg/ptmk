import datetime

create_table_request = """ 
        CREATE Table IF NOT EXISTS users(
        user_id SERIAL PRIMARY KEY,
        full_name VARCHAR(128) NOT NULL,
        date_of_birth DATE NOT NULL,
        gender VARCHAR(5) NOT NULL);
        """

insert_new_line_request = """
        INSERT INTO users (full_name, date_of_birth, gender)
        VALUES (%s, %s, %s);
        """

get_output_from_table_full_name_with_date_of_birth = """
        SELECT DISTINCT full_name, date_of_birth FROM users
        ORDER BY full_name
        """

get_output_from_table_fcs_date_of_birth_gender_full_years = """
        SELECT full_name, date_of_birth, gender, date_part('year', age(date_of_birth::date)) FROM users
        """

full_table = """
        SELECT * FROM users
        """

result_selection = """
        SELECT * FROM users
        WHERE gender = 'M' AND full_name LIKE 'F%'
        """
