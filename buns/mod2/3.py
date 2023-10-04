str = input()
a = 0
b = 0
c = 0
k = 0
len1 = 0
len2 = 0
for char in str:
    if char == ' ':
        k += 1
    if k == 0:
        len1 += 1
    if k == 1:
        len2 += 1
        
a = int(str[:len1])
b = int(str[len1 + 1: len1+len2])
c = int(str[len1 + len2 + 1:])

if((a >= b) & (a >= c)):
    if(b >= c):
        print(b)
    else:
        print(c)
elif((b >= a) & (b >= c)):
    if(a >= c):
        print(a)
    else:
        print(c)
elif((c >= a) & (c >= b)):
    if(a >= b):
        print(a)
    else:
        print(b)
