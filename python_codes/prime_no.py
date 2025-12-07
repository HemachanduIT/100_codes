# input:
#     5
# output:
#     5 is prime
# <------------------------------>
# n=int(input())
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#     print(n,'is prime')
# else:
#     print(n,'is not prime')
# <------------------------------------->
from math import sqrt
no=int(input())
flag=True
for i in range(2,int(sqrt(n))+1):
    if no%i==0:
        flag=False
        break
if flag:
    print(no,'is prime')
else:
    print(no,'is not prime')