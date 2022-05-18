class Overloading:
 def print_arg(self,name=None,age=None):
  if name!=None and age==None:
   print("Your name is ",name)
  if name!=None and age!=None:
   print("Your name is ",name, "and your age is ",age)
  if name==None and age==None:
   print("Hello")

o=Overloading()
print("select one option")
print("1.No argument\n2.With one argument\n3.With two arguments")
ch=int(input("Enter your choice :"))
if ch==1:
 o.print_arg()
if ch==2:
 o.print_arg("abhi")
if ch==3:
 o.print_arg("abhi",22)
