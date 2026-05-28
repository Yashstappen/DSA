N = int(input("N:"))
def func(N):
    if(N==1):
        return 1
    return (N * func(N-1))
Fact = func(N)
print(Fact)
