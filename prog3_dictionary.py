dict = {}
class Employee:
 def __init__(self):
  self.name = input("Enter your name :")
  self.addr = input("Enter your address :")
  self.pan = input("Enter your pan number :")
  self.basic = input("Enter basic pay :")
  self.da = self.basic * 0.5
  self.ha = self.basic * 0.75
  self.tda = self.basic * 1
  self.gross = self.da + self.ha + self.tda
  self.net = self.gross - self.tda
  self.update()
  print("Data Succesfully added")

 def update(self):({self.name:{
  "Name" : self.name,
  "Address" : self.addr,
  "PAN" : self.pan,
  "Basic" : self.basic,
  "DA" : self.da,
  "HA" : self.ha,
  "TDA" : self.tda,
  "Gross" : self.gross,
  "Net" : self.net

	}})

 def printout(self):
  print("Employee Name is	:",self.name)
  print("Employee Address is	:",self.addr)
  print("Employee PAN is	:",self.pan)
  print("Employee Basic Salary	:",self.basic)
  print("Employee Gross Salary	:",self.gross)
  print("Employee Net Salary	:",self.net)

 def search(self,key):
  if key in dict.keys():
   print dict.item(key)
  else:
   print("Invaid key")

emp = Employee()
print("Select one option")
print("1. Add-data, 2. Output , 3. search, 4. exit")
ch = input("Enter the choice number : ")
if ch==1:
	emp.__init__()
if ch==2:
	emp.printout()
if ch==3:
	s = str(input("type the key to search : "))
	emp.search(s)

