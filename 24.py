a = int(input())
a3 = a % 10
a2 = (a % 100) // 10
a1 = a // 100
print(a)
print(a1, a3, a2, sep="")
print(a2, a1, a3, sep="")
print(a2, a3, a1, sep="")
print(a3, a1, a2, sep="")
print(a3, a2, a1, sep="")