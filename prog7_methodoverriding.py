class employee:
    raise_amt = 1.04
    def __init__(self,first,last,empid,pay):
        self.first = first
        self.last = last
        self.empid = empid
        self.pay = pay
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def display_details(self):
        print("First Name is :",self.first)
        print("Last Name is :",self.last)
        print("Employee ID is :",self.empid)
        print("Your Pay after aprisal is :",self.pay)

class developer(employee):
    raise_amt = 1.05

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class manager(employee): 
    raise_amt = 1.06

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp1 = manager("Abhi","Achar",101,50000)
emp2 = developer("Uday","Achar",201,25000)
print(emp1.first," Pay before aprisal :",emp1.pay)
print(emp2.first," Pay before aprisal :",emp2.pay)
emp1.apply_raise()
emp2.apply_raise()
print(emp1.display_details())
print(emp2.display_details())
