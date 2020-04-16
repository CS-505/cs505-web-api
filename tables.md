# cs505-web-api
import mysql.connector
import csv
import MySQLdb
import pandas as pd

#Mysql@localhost:3306
#craete a connection to the mySQL db
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="12345678"
)
# creating db
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

#creating tables
mycursor.execute("CREATE TABLE Patient (mrn VARCHAR(255), location_id VARCHAR(255), patient_status_code VARCHAR(255))")
mycursor.execute("CREATE TABLE zip_alert (zip_code VARCHAR(255), is_alert VARCHAR(255), last_count VARCHAR (255))")
mycursor.execute("CREATE TABLE unique_zip_codes (zip_code VARCHAR(255))")
# importing the csv file 
dis=pd.read_csv(r'/Users/adelalluhayb/Desktop/COVID-19/kyzipdistance.csv')
nique=mycursor.execute("SELECT DISTINCT zip_from INTO unique_zip_codes FROM dis")
new_zip_alert=mycursor.execute("INSERT INTO zip_alert (zip_code) SELECT zip_code FROM unique_zip_codes")
mycursor.execute("INSERT INTO ")



mydb.close()
