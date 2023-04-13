import mysql.connector as mysql

try:
    connection = mysql.connect(host='localhost',
                               database='test',
                               user='root',
                               password='My$ql4dmin')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        createTable = """CREATE TABLE dept ( 
                             Id int(11) NOT NULL AUTO_INCREMENT,
                             Name varchar(250) NOT NULL,
                             StudentCount int(11) NOT NULL,
                             StaffCount int(11) NOT NULL,
                             PRIMARY KEY (Id)) """

        addToTable = """INSERT INTO dept(Name,StudentCount,StaffCount) values("Comp",500,120),("IT",180,50);"""
        result = cursor.execute(createTable)
        print("Dept Table created successfully")
        cursor.execute(addToTable)
        print("Values added in Dept Table")


finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
