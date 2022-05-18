import time
def timeit(func):
 def timeout(*args, **kw):
  print("*************Before timeit  decorator***********")
  print(" ")
  time_s = time.time()
  result = func(*args, **kw)
  time_e = time.time()
  minutes,seconds = divmod((time_e-time_s), 60)
  print(minutes,seconds)
  print("time taken %8.2f" % ((time_e-time_s)*10**6))
  print(" ")
  print("*************After timeit decorator*************")
  return result
 return timeout

@timeit
def fib():
        a,b=0,1
        while(1):
                yield a
                a,b=b,a+b

num=int(input("Enter the number for fibonacci series : "))
fibonacci = fib()

for x in range(num):
        print (next(fibonacci))

