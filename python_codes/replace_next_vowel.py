s=input().lower()
v=['a','e','i','o','u']
res=''
for i in range(len(s)):
    if s[i] in v:
        for j in range(len(s)-1):
            if s[i]==v[j]:
                res+=v[j+1]
    else:
        res+=s[i]
print(res)

