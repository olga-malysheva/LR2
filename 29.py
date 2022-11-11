n = int(input())
num3 = n % 10
num2 = ((n % 100) // 10) * 100
num1 = (n // 100) * 10
print(num3 + num1 + num2)