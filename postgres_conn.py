import psycopg2


def pg_conn():
    try:
        return psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="BBoH$$.")
    except psycopg2.DatabaseError as err:
        print(err)