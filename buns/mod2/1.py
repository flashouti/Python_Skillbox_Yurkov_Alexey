str = input()
a = 0
b = 0
k = 0
for char in str:
    if char == ',':
        a = int(str[:k])
        b = int(str[k + 2:])
    k += 1
print(a % b)
