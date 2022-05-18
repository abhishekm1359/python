class STUDENT:
 def __init__(self):
  self.usn = ""
  self.name=""
  self.age=""

 def getdata(self):
  self.usn = int(input("Enter your USN Number : "))
  self.name = input("Enter your Name :")
  self.age = int(input("Enter your age :"))


class UGSTUDENT(STUDENT):
 def __init__(self):
  self.sem = ""
  self.fees=""
  self.stipend=""

 def getugdata(self):
  self.sem = int(input("Enter your semester : "))
  self.fees = int(input("Enter your college fees :"))
  self.stipend = int(input("Enter your stipend :"))

 def display_ug(self):
  print("Your Name is 		:",self.name)
  print("\nYour USN is 		:",self.usn)
  print("\nYour Age is 		:",self.age)
  print("\nYour Semester is 	:",self.sem)
  print("\nYour College Fee is 	:",self.fees)
  print("\nYour stipend is 	:",self.stipend)

class PGSTUDENT(STUDENT):
 def __init__(self):
  self.sem = ""
  self.fees=""
  self.stipend=""

 def getpgdata(self):
  self.sem = int(input("Enter your semester : "))
  self.fees = int(input("Enter your college fees :"))
  self.stipend = int(input("Enter your stipend :"))

 def display_pg(self):
  print("Your Name is           :",self.name)
  print("\nYour USN is          :",self.usn)
  print("\nYour Age is          :",self.age)
  print("\nYour Semester is     :",self.sem)
  print("\nYour College Fee is  :",self.fees)
  print("\nYour stipend is      :",self.stipend)


SU=STUDENT()
PG=PGSTUDENT()
UG=UGSTUDENT()

while True:
 print("\n-----------------------------------------------------------------------------------------------------------------------------")
 print("select one option")
 print("1. Enter UG Student Details \n2. Enter PG Student Details\n3. Print UG Student Details\n4. Print PG Student Details\n5. Exit")
 ch = int(input("Enter your choice :"))
 if ch==1:
  UG.getdata()
  UG.getugdata()
 if ch==2:
  PG.getdata()
  PG.getpgdata()
 if ch==3:
  UG.display_ug()
 if ch==4:
  PG.display_pg()
 if ch==5:
  break
 print("\n-----------------------------------------------------------------------------------------------------------------------------")
