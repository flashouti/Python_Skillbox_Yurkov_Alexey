s = input()
gl = 'ёуеыаоэяию'
sogl = 'бвгджзйклмнпрстфхцчшщ'
countGl = 0
countSogl = 0
for char in s.lower():
    if (char in gl):
        countGl += 1
    elif (char in sogl):
        countSogl += 1
print(countGl, countSogl)
