def strongno(n):
    k=n
    s=0
    while n!=0:
        f=1
        r=n%10
        for i in range(1,r+1):
            f=f*i
        s+=f
        n//=10
    if s==k:
        return f"{k} is strong no"
    else:
        return f"{k} is not strong no"
        
n=int(input())
print(strongno(n))