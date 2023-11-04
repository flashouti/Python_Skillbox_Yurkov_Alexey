def get_armstrong_numbers():
    for num in range(10, 100000):
        order = len(str(num))
        total = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            total += digit ** order
            temp //= 10
        if num == total:
            yield num

n = int(input("Enter the number: "))
for armstrong_number in get_armstrong_numbers():
    print(armstrong_number, end=' ')
    n -= 1
    if n == 0:
        break
