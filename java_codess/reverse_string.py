# input:
#     chandu
# output:
#     udnahc
s=input()
# print(s[::-1])
rev=''
# for i in s:
#     rev=i+rev
# print(rev)
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print(rev)
    