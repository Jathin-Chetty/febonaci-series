import math

def d(x):
    s = int(math.sqrt(x))
    return s * s == x
def isFibonacci(n):
    return d(5 * n * n + 4) or d(5 * n * n - 4)
w=int(input("No. of inputs you wanna take: "))
for i in range(1,w+1):
    n=int(input("Input: "))
    x=isFibonacci(n)
    if x is True:
        print(n,"is a valid ")
    else:
        print(n, "is invalid ")