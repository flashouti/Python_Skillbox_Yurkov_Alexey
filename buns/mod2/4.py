a = float(input())
bin1 = ''
oct1 = ''
hex1 = ''
symbolsHex = "0123456789ABCDEF"
if a != int(a):
    print("Неверный ввод")
else:
    new2 = int(a)
    new8 = int(new2)
    new16 = int(new2)
    if new2 <= 0:
        print("Неверный ввод")
    else:
        while new2 > 0:
            bin1 = str(new2 % 2) + bin1
            new2 = new2 // 2
        while new8 > 0:
            oct1 = str(new8 % 8) + oct1
            new8 = new8 // 8
        while new16 > 0:
            hex1 = symbolsHex[new16 % 16] + hex1
            new16 = new16 // 16
print(bin1, oct1, hex1)
