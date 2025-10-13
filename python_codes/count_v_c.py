# input:
#     hema chandu
# output:
#     vowel count is 4
#     consonent count is 7
s=input()
vc,cc=0,0
for i in s:
    if i in 'aeiouAEIOU':
        vc+=1
    else:
        cc+=1
print('vowel count is',vc)
print('consonent count is',cc)