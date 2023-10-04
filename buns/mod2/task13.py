s = str(input())
sum0 = 0
sum1 = 0
for i in range(0, len(s), 2):
    sum0 += int(s[i])
for i in range(1, len(s), 2):
    sum1 += int(s[i])

if((sum1 * 3 + sum0) % 10 == 0):
    print('yes')
else:
    print('no')
    
