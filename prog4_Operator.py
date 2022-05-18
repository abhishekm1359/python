
class Operator:
 def __init__(self):
  self.list=[]
 def getelement(self):
  self.n=int(input("enter max size of list "))
  for i in range(self.n):
   self.list.append(int(input("enter the element :")))
  print(self.list)
 def __add__(self,other):
  self.new_list=[]
  self.zipped_list=zip(self.list,other.list)
  for i in self.zipped_list:
   self.new_list.append(i[0]+i[1])
  print("overloaded addition of lists :",self.new_list)
 def __sub__(self,other):
  self.new_list=[]
  self.zipped_list=zip(self.list,other.list)
  for i in self.zipped_list: 
   self.new_list.append(i[0]-i[1]) 
  print("overloaded substraion of two list :",self.new_list)
 def __mul__(self,other):
  self.new_list=[]
  self.zipped_list=zip(self.list,other.list)
  for i in self.zipped_list: 
   self.new_list.append(i[0]*i[1]) 
  print("overloaded multiplication of lists :",self.new_list) 
 def __floordiv__(self,other):
  self.new_list=[]
  self.zipped_list=zip(self.list,other.list)
  for i in self.zipped_list: 
   self.new_list.append(i[0]//i[1]) 
  print("overloaded floor divistion of lists :",self.new_list) 
 
