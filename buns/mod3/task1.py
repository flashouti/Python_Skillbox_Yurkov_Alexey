a, b, c = map(int, input().split())
sr = (a + b + c) - max(a, b, c) - min(a, b, c)
print(sr)

