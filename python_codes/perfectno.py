# input:
#     28
#     24
# output:
#     28 is perfect no
#     24 is not perfect
def perfect(n):
    s=0
    # for i in range(1,n//2+1):
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        return f"{n} is perfect no"
    else:
        return f"{n} is not perfect"
n=int(input())
print(perfect(n))