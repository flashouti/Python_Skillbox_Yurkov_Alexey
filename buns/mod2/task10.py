s = input()
result = ''
for i in range(0, len(s)):
    if (s[i] == ' '):
        result += s[i - 1]
        
result += s[len(s) - 1]

print(result)
