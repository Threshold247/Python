import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

connection = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="Abcd1234"
)


