a = int(input())
a2 = a % 10
a1 = a // 10
if a1 > a2:
    print('Первая цифра больше')
elif a1 < a2:
    print('Вторая цифра больше')
elif a2 == a1:
    print('Цифры одинаковы')