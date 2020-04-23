import MySQLdb


mydb = MySQLdb.connect(host='rabowl2.cs.uky.edu',
    user='root',
    passwd='password',
    db='hospital_info')
    

cursor = mydb.cursor()

#drop tables if exist
cursor.execute("DROP TABLE IF EXISTS zipcode_distances")
cursor.execute("DROP TABLE IF EXISTS hospital_data") 
        
# create table
cursor.execute("CREATE TABLE zipcode_distances(zip_from varchar(5),zip_to varchar(5),distance decimal(20,15))")
mydb.commit()

#import csv
cursor.execute("LOAD DATA LOCAL INFILE './kyzipdistance.csv' INTO TABLE zipcode_distances FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES")
mydb.commit()

# create table
cursor.execute("CREATE TABLE hospital_data (hospital_id varchar(9),hospital_zip varchar(5),beds_available int)")
mydb.commit()

#import csv
cursor.execute("LOAD DATA LOCAL INFILE './hospitals.csv' INTO TABLE hospital_data FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES")
mydb.commit()

#add column for beds occupied
cursor.execute("ALTER TABLE hospital_data ADD bed_occupied int DEFAULT (0)")
mydb.commit()

# disconnect from server 
mydb.close() 

print("success")
