import mysql.connector
import sys
import os

config = {
	'host':'127.0.0.1',
	'user':'root',
	'password':'jordanizumi',
	'database':'shared_data'
}

cnx = mysql.connector.connect(**config)

# creating database_cursor to perform SQL operation
db_cursor = cnx.cursor()
# executing cursor with execute method and pass SQL query

# create a new database once, comment afterward
# db_cursor.execute("CREATE DATABASE shared_data CHARACTER SET utf8")

#print all databases
db_cursor.execute("SHOW DATABASES")
for db in db_cursor:
	print(db)

# Navigate to the directory with the SDY files
# assumes they are stored within a folder named 'data'
BASE_DIR = os.getcwd()
study56 = "SDY56-DR33_MySQL"
data_directory = os.path.join(BASE_DIR,"data", study56, "scripts")
os.chdir(data_directory)
print(os.getcwd()) # for debugging

db_cursor.execute("./createLkSchema.sh", params=config)
print()

db_cursor.execute("./createResearchSchema.sh", params=config)

db_cursor.execute("./loadLkData.sh", params=config)

db_cursor.execute("./loadResearchData.sh", params=config)

print("Done loading hopefully!")
