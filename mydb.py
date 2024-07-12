import mysql.connector
from mysql.connector import Error

try:
    # Establish a connection to the MySQL database
    dataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Mari@123'
    )
    
    if dataBase.is_connected():
        print("Connected to MySQL Server version:", dataBase.get_server_info())

        # Create a cursor object
        cursorObject = dataBase.cursor()

        # Execute a command to create a new database
        cursorObject.execute("CREATE DATABASE IF NOT EXISTS mari")
        print("Database 'mari' created successfully.")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Close the database connection
    if 'dataBase' in locals() and dataBase.is_connected():
        cursorObject.close()
        dataBase.close()
        print("MySQL connection is closed.")
