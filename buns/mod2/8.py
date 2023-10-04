s = str(input())
str1 = ''
symbol = ''
k = 0;
for char in s:
    if char == ',':
        str1 = s[:k]
        symbol = s[k+1:]
    k += 1   
if(str1[0] == symbol):
    print(1)
else:
    print(0)
