def bubblesort(s):
    flag=True
    while flag:
        flag=False
        for i in range(len(s)-1):
            if s[i]>s[i+1]:
                s[i],s[i+1]=s[i+1],s[i]
                flag=True
    return s
    
s=list(map(int,input().split()))
print(bubblesort(s))