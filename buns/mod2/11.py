s = str(input())
flag = False
for i in range(1, len(s)):
    if(s[i] in s[:i]):
        flag = True
print(flag)
        
