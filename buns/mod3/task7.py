s = input().split()
if len(s) != len(set(s)): print(True)
else: print(False)