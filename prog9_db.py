import mysql.connector
db=mysql.connector.connect(host="172.16.34.105" , user="mca071" , password="mca071" , db="mca071")
cursor=db.cursor()
def table():
        try:
         cursor.execute("create table tab2(name varchar(20),address varchar(30))")
         print("\ntable created successfully")
        except:
         print("\n table already exists")
def insert():
        sql =("INSERT INTO tab2 value('abhishek','Bangalore'),('uday','Mysore'),('Ajith','Mangalore')")
        cursor.execute(sql)
        print("\n New row inserted")

def display():
        print("_________Start of Data_______________")
        i=cursor.execute("SELECT * FROM tab2 ")
        for i in cursor:
                print (i)
        print("__________End of Data_________________")

while True:
        print("***********************************************************************************")
        print("Select any one choice")
        print(" 1-Create Table \n 2-Insert into table \n 3-Display Table \n 0-Exit \n")
        ch = int(input("Enter your choice here : "))
        if ch==1:
                table()
        elif ch==2:
                insert()
        elif ch==3:
                display()
        elif ch==0:
                break

