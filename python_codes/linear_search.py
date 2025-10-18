def linear_search(s,key):
    flag=True
    for i in s:
        if i==key:
            flag=False
            return f"{key} found"
    if flag:
        return f"{key} not found"  
        
        
s=list(map(int,input().split()))
key=int(input())
print(linear_search(s,key))