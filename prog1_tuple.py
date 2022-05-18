tuple1=('a','b','c','d','e')
tuple2=('RVCE',304)
print("\n1 Concatination of tuples is :",tuple1 + tuple2)
print("\n2 Repetation of tuples is : ",tuple2*2)
print("\n3 String Membership of 'a' in tuple1 is : ",'a' in tuple1)
print("\n4 String Membership of 'h' in tuple1 is : ",'h' in tuple1)
print("\n5 Iteration of tuple1")
for i in tuple1: 
 print(i)
print("\n6 Length of tuple1 is : ",len(tuple1))
print("\n7 Maximum Value of tuple1 is : ",max(tuple1))
print("\n8 Range slice of tuples is :",tuple1[0:3])
print("\n9 Slicing of tuple is : ",tuple1[2])
del tuple1
tuple1=()
print("\n10 Deletion of tuple1 : ",tuple1)

