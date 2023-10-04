str = input()
count1 = 0;
count0 = 0;
for char in str:
    if char == '1':
        count1 += 1
    else:
        count0 += 1
if(count1 == count0):
    print('yes')
else:
    print('no')
