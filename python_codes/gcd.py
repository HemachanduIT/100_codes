# input:
#     5 15
# output:
#     the gcd of 5 and 15 is 5
# <---------------------------------------------->
# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# a,b=map(int,input().split())
# print("the gcd of",a,"and",b,"is",gcd(a,b))
# <------------------------------------------------------>
# from math import gcd
# print(gcd(15,5))
# <----------------------------------------------------->
a,b=10,20
# while b!=0:
#     temp=b
#     b=a%b
#     a=temp
# print(a)
# <------------------------------------------------>
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print(a)
        