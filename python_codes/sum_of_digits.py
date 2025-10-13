# input:
#     12345
# output:
#     15
# def summ(n):
#     s=0
#     while n!=0:
#         s+=n%10
#         n//=10
#     return s
# n=int(input())
# print(summ(n))
# <---------------------------->
res=0
n=int(input())
s=str(n)
for i in s:
    res+=int(i)
print(int(res))