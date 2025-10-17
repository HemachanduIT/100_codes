def charcount(s,key):
    c=0
    for i in s:
        if i==key:
            c+=1
    return c
s=input()
key=input()
print(charcount(s,key))
