def start():
 A=[2,1,4,5,3]
 print ("list A")
 print (A)
 print ("\n1. Popping a element from A") 
 A.pop()
 print (A)
 print ("\n2. Appending a elemnet to list A")
 A.append(6)
 print (A)
 print ("\n3. Sorting list A")
 A.sort()
 print (A)
 print("\n4. In Value")
 print (2 in A)
 B = [11,12,13]
 print("\n5. Concate of Lists")
 C = A+B
 print (C)
 print ("\n6. Repetation")
 print (A*2)
 print ("\n7. Lenth of List")
 print (len(C))
 print( "\n8. Range slice")
 print (A[0:3])
 print ("\n9. Maximum value")
 print (max(A))
 print("\n10. Iteration")
 for i in A:
  print(i)
start()
