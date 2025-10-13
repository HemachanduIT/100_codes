import math
def armstrong(n):
    k=n
    # c=int(math.log10(n))+1
    c=len(str(n))
    s=0
    while n!=0:
        r=n%10
        s+=math.pow(r,c)
        n//=10
    if s==k:
        return "Armstrong"
    else:
        return "not armstrong"
        
n=int(input())
print(armstrong(n))