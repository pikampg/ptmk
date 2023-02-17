import psycopg2

host = "localhost"
user = "postgres"
password = "123"
db_name = "postgres"

connection = psycopg2.connect(
        database=db_name,
        host=host,
        user=user,
        password=password
    )
cursor = connection.cursor()