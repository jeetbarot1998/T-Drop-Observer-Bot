import os

import psycopg2
from config import SQL_ALCHEMY_DB_URL
try:
    # Connect to an existing database
    # FOR LOCAL HOST
    connection = psycopg2.connect('postgres://ucmdkokipuljyi:3911ddbd4da67f64a3cf80355b0bf7a1cb2221337a43e32c83851f49eeffcfba@ec2-3-226-211-228.compute-1.amazonaws.com:5432/ddvlni5bs2bil6')
    #  FOR SERVER
    # connection = psycopg2.connect(os.environ['DATABASE_URL'])
    # Create a cursor to perform database operations
    cursor = connection.cursor()
    cursor.execute("SELECT *FROM movie_entries")
    purchase_datetime = cursor.fetchall()
    print('here====================',purchase_datetime)
    # Print PostgreSQL details
    # print("PostgreSQL server information")
    # print(connection.get_dsn_parameters(), "\n")
    # # Executing a SQL query
    # cursor.execute("SELECT version();")
    # # Fetch result
    # record = cursor.fetchone()
    # print("You are connected to - ", record, "\n")

except Exception as error:
    print("Error while connecting to PostgreSQL", error)