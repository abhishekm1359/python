class employee:
 raise_amt = 1.05

 def __init__(self,first,last,empid,pay):
  try:
   self.first = first
   self.last = last
   self.empid = int(empid)
   self.pay = int(pay)
  except NameError:
   print("Enter input in strings")
 def apply_raise(self):
  self.pay = int(self.pay * raise_amt)

 def display(self):
  print("Your First name is :",self.first)
  print("Your Last name is :",self.last)
  print("Your Employee ID is :",self.empid)
  print("Your Salary after apprisal is :",self.pay)

class manager(employee):
 raise_amt = 1.10

 def apply_raise(self):
  self.pay = int(self.pay * self.raise_amt)

class developer(employee):
 raise_amt = 1.10

 def apply_raise(self):
  self.pay = int(self.pay * self.raise_amt)
print("**************************************************************************************")
try:
 emp1 = manager("Abhi","Achar",1001,55000)
 emp2 = developer("Uday","Kumar",2001,30000)

 print(emp1.first,"salary before raise :",emp1.pay)
 print(emp2.first,"salary before raise :",emp2.pay)
 print("---------------------------------------------------------------------")

 emp1.apply_raise()
 emp2.apply_raise()

 emp1.display()
 print("---------------------------------------------------------------------")
 emp2.display()
 print("**************************************************************************************")
except NameError:
 print("Enter First and Last names in strings")


