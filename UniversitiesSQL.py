import csv
import mysql.connector

Universities = mysql.connector.connect(host="localhost",user="root",password="P3dr0mysql",database="Universities")
myCursor = Universities.cursor(buffered=True)

with open("College4.csv") as File:
    fHand = csv.reader(File,delimiter=",")
    
    for line in fHand:
        
        formula="INSERT INTO Information(school_name,url,state) VALUES (%s, %s, %s)"
        info = (line[0],line[1],line[2])
        myCursor.execute(formula,info)

    Universities.commit()
