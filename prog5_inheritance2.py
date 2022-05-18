class STUDENT:
 def __init__(self):
  self.usn=""
  self.name=""
  self.age=""

 def getdata(self):
  self.usn=int(input("Enter Your USN number :"))
  self.name=input("Enter your name :")
  self.age=int(input("Enter your age :"))

class STUDENT1(STUDENT):
 def __init__(self):
  self.sub1=""
  self.sub2=""
  self.sub3=""
  self.sub4=""
  self.sub5=""

 def getmarks_and_calc(self):
  #flag=0
  self.sub1=int(input("Enter your Subject1 marks :"))
  self.sub2=int(input("Enter your Subject2 marks :"))
  self.sub3=int(input("Enter your Subject3 marks :"))
  self.sub4=int(input("Enter your Subject4 marks :"))
  self.sub5=int(input("Enter your Subject5 marks :"))

  #if(self.sub1<40 or self.sub2<40 or self.sub3<40 or self.sub4<40 or self.sub5<40):
   #flag=1
  self.totalmarks = (self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5)
  self.percentage = (self.totalmarks/500)*100

class STUDENT2(STUDENT1):
 def display(self):
  print("Your name is 		:",self.name)
  print("Your USN is 		:",self.usn)
  print("Your age is 		:",self.age)
  print("Your Total Marks is 	:",self.totalmarks)
  print("Your Percentage is 	:",self.percentage)

SU = STUDENT2()
while True:
 print("\n-----------------------------------------------------------------------------------------")
 print("Select your option")
 print("1. Add Student Details\n2. Add Subject marks\n3. Display Result\n4. Exit")
 ch = int(input("Enter your choice :"))
 if ch==1:
  SU.getdata()
 if ch==2:
  SU.getmarks_and_calc()
 if ch==3:
  #if flag==1:
   #print("Student ",self.name,"is Failed in one of the subject")
  #else:
   SU.display()
 if ch==4:
  break
