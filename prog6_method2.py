from multipledispatch import dispatch


@dispatch(str,int)
def print_arg(name,age):
         print("Your name is ",name, "and your age is ",age)

@dispatch(str)
def print_arg(name):
        print("Your name is :",name)

@dispatch(int)
def print_arg(age):
       print("your age is :",age)

#o=overloading()
print_arg("abhi",22)
print_arg("abhi")
print_arg(22)
