s = str(input())
symbols = ' ()-'
result  = ''
for ch in s:
    if (ch not in symbols):
        result += ch

print(result)
