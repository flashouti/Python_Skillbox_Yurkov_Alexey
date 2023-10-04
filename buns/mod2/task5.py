
str = input()
letter = 0
a = 0
k = 0
for char in str:
    if char == ',':
        letter = str[:k]
        a = int(str[k + 1:])
    k += 1

print(chr(97 + ((ord(letter) - 97) + a)% 26))
