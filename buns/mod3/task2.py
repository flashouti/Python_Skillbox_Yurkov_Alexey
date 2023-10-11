n = int(input())
bin1, oct1, hex1 = bin(n)[2:], oct(n)[2:], hex(n)[2:]
print("Неверный ввод") if n < 1 else print(bin1, oct1, hex1)