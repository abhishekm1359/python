def start_set():
 X = {25,23,21}
 Y = {25,24,22}
 print ("Set X :")
 print (X)
 print("\n")
 print ("Set Y :")
 print (Y)
 print("\n")

 print ("1. 22 in Set X")
 print (22 in X)
 print("\n")

 print ("2. Length of Set X")
 print (len(X))
 print("\n")

 print ("3. X - Y")
 print (X-Y)
 print("\n")

 print ("4. Contains")
 print (X.__contains__(21))
 print("\n")

 print("5. Intersection")
 print(X.intersection(Y))
 print("\n")

 print ("6. Clearing elements in set Y")
 Y.clear()
 print (Y)
 print("\n")

 print ("7. pop element from X")
 X.pop()
 print (X)
 print("\n")

 print ("8. add element to X")
 X.add(29)
 print (X)
 print("\n")

 print("9. Size in bytes")
 print(X.__sizeof__())
 print("\n")

 print("10. Deleting a set")
 del (X)
 print("\n")

start_set()
