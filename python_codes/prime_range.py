# input:
#     2
#     15
# output:
#     2 3 5 7 11 13

from math import sqrt
start=int(input())
stop=int(input())
# <---------------------------------->
# for i in range(start,stop):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         print(i,end=' ')
# <-------------------------------->
# if start==0 or start==1:
#     print()
for i in range(start,stop):       
    for j in range(2,int(sqrt(i))+1):
        if i%j==0:
            flag=False
            break
    else:
        print(i,end=' ')

            