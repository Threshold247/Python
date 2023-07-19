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
sql = '''SELECT * FROM tasks'''
connection = psycopg2.connect(**params)

# reading data from the database
cur = connection.cursor()
cur.execute(sql)
# print the number of rows
print(cur.rowcount)
# print the data of each row
row = cur.fetchone()
print(row)
cur.close()

