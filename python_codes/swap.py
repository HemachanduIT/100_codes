a,b=10,20
print('Before swap',a,b)
# a,b=b,a
# print('after swap',a,b)
# <-------------------------------->
a=a+b
b=a-b
a=a-b
print('after swap',a,b)
