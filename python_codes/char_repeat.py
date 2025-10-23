s=input()
res=''
c=1
for i in range(len(s)-1):
    #aabbc
    
    if s[i]==s[i+1]:
        c+=1
    else:
        res+=s[i]+str(c)
        c=1
else:
    c=1
    res+=s[-1]+str(c)
    
print(res)

# input/output:
#aaabbbccdde
# a3b3c2d2e1
        
    