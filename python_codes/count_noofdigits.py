n=int(input())
# print(len(str(n)))
# <----------------------------------->
# c=0
# while n!=0:
#     n//=10
#     c+=1
# print(c)
# <------------------------------------>
import math
c=int(math.log10(n))+1
print(c)