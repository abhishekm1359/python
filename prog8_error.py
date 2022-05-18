oldfile = input("Enter the name of existing file :")
newfile = input("Enter the name of new file :")

try:

 file=open(oldfile,'r')
 content=file.read()
 print("Content in file is :",content)
 file=open(newfile,'w')
 file.write(content)
 print("Copied content is :",content)

except IndentationError:
 print("Mistake in spacing")
except SyntaxError:
 print("Syntax Error")
except FileNotFoundError:
 print("Given file name is not found")
except NameError:
 print("Some error in name")
except IOError:
 print("Input Output Error Occured")
else:
 print("Copy Successfull")
 file.close()
