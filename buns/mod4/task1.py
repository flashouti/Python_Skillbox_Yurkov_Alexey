arr = []
for i in input().split(' '):
    arr.append(int(i))


def check_numbers(numbers):
    if len(set(numbers)) == 1:
        return "Все числа равны"
    elif len(set(numbers)) == len(numbers):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"


result = check_numbers(arr)
print(result)