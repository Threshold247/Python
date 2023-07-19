import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(".env")
params = {
    "host": os.getenv("HOST"),
    "database": os.getenv("DATABASE"),
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD")
    }

# reading data from the database
sql = '''SELECT * FROM tasks'''
connection = psycopg2.connect(**params)
cur = connection.cursor()
cur.execute(sql)
# print the number of rows
print(cur.rowcount)
# print the data of each row.
row = cur.fetchone()
print(row)
row_id = row[0]
print(f"id: {row_id}")
cur.close()

# adding data to the database
# sql = '''INSERT INTO Tasks (description, "day", reminder)
#         VALUES ('Input from text box', 'input from date text box', false) '''
# connection = psycopg2.connect(**params)
# cursor = connection.cursor()
# cursor.execute(sql)
# connection.commit()
# cursor.close()
# connection.close()
