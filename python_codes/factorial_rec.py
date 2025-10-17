def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
    
    # f=1
    # for i in range(1,n+1):
    #     f=f*i
    # return f
n=int(input())
print(fact(n))