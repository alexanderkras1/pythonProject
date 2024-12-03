# input("Введите 4-х значное число:")

num = input("Введите 4-х значное число:")
num = int(num)
print(num // 1000)
print(num // 100 % 10)
print(num // 10 % 10)
print(num % 100 % 10)

