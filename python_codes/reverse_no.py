# input:
#     123
# output:
#     321
n=int(input())
r=0
while n!=0:
    r=r*10+n%10
    n//=10
print(r)