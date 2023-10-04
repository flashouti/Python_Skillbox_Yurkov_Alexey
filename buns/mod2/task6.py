str = input()
dot = '.'
domain = ''
for i in range(len(str)-1, -1, -1):
    if str[i] != dot:
        domain = str[i] + domain
        if i == 0:
            print(domain)
            break
    else:
        print(domain)
        domain = ''
