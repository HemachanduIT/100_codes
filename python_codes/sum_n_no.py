def summ_no(n):
    # s=n*(n+1)//2
    s=0
    for i in range(1,n+1):
        s+=i
    return s
n=int(input())
print(summ_no(n))