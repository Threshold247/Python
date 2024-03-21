import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(".env")


class Database:
    def __init__(self):
        self.params = {
            "host": os.getenv("HOST"),
            "database": os.getenv("DATABASE"),
            "user": os.getenv("USER"),
            "password": os.getenv("PASSWORD")
            }

# reading data from the database
    def get_data(self):
        sql = '''SELECT * FROM tasks'''
        connection = psycopg2.connect(**self.params)
        cur = connection.cursor()
        cur.execute(sql)
        # print the number of rows
        # print(cur.rowcount)
        # print the data of each row.
        row = cur.fetchall()
        # print(row)
        cur.close()
        return row

    def get_row_id(self):
        sql = '''SELECT * FROM tasks'''
        connection = psycopg2.connect(**self.params)
        cursor = connection.cursor()
        cursor.execute(sql)
        # print the data of each row.
        row = cursor.fetchall()
        print(row)

        for task_id in row:
            print(f"{task_id[0]}")
        cursor.close()

# adding data to the database
    def adding_data(self, task_description, date, reminder):
        sql = '''INSERT INTO Tasks (description, "day", reminder) VALUES (%s, %s, %s)'''
        vals = (task_description, date, reminder)

        connection = psycopg2.connect(**self.params)
        cursor = connection.cursor()
        cursor.execute(sql, vals)
        connection.commit()
        print(cursor.rowcount, "record inserted.")
        cursor.close()
        connection.close()

# delete data from the database

    def delete_data(self, task_id):
        sql = f'''DELETE FROM Tasks WHERE id = {task_id}'''

        connection = psycopg2.connect(**self.params)
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        print(f"{task_id} deleted.")
        cursor.close()
        connection.close()
