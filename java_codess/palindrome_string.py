# input:
#     madam
# output:
#     madam is palindrome
s=input()
if s==s[::-1]:
    print(s,'is palindrome')
else:
    print(s,'is not palindrome')