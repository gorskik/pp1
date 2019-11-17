

def fib(x): 
    if (x == 1): 
        return 1
    else: 
        return fib(x-1)+fib(x-2)

x=0
while x<20:
    print(fib(x))
    x+=1
    
