import mysql.connector as mc 
from dbconfig import Config
mydb=mc.connect(host=Config.host,user=Config.user,passwd=Config.passwd)
mydb.autocommit=True
mycur=mydb.cursor()


mycur.execute(("""CREATE DATABASE IF NOT EXISTS vote"""))
mycur.execute(("USE vote"))
mycur.execute(("""CREATE TABLE IF NOT EXISTS voter_data(name varchar(20) NOT NULL,age INT(3) NOT NULL,uid INT(30) PRIMARY KEY NOT NULL,region varchar(20) NOT NULL,voted_to varchar(20) NOT NULL)"""))



with open(r"Data\voters_data.csv") as vd:
    trash=vd.readline() #readfields 
    while True:
        r_data=vd.readlines()
        data=[] #main data in str
        for i in range(1,len(r_data),2): #neglect gaps in data 
            data.append(r_data[i])
        for j in data:
            m_data=j  #main data ie string
            sql_data=j.strip().split(',') #removed spaces and \n
            

            print(sql_data)
            print("DATA UPLOADED TO SQL DATABASE SUCCESSFULLY!")

            while data:
                try:
                    mycur.execute(("insert into voter_data(name,age,uid,region,voted_to) values('{}',{},{},'{}','{}')".format(sql_data[0],sql_data[1],sql_data[2],sql_data[3],sql_data[4])))
        
                except:
                    None
                    break
            
                 