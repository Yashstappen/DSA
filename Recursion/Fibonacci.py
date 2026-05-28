N = int(input())

def fib(Num):
    if(Num==0 or Num==1):
        return Num
    return fib(Num-1)+fib(Num-2)

def call(N):
    fib(N)
    return fib(N)

print(call(N))