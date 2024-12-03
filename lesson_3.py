number = int(input("Введите 5-ти значное число: "))

reversed_number = 0

reversed_number += (number % 10) * 10000
number = number // 10

reversed_number += (number % 10) * 1000
number = number // 10

reversed_number += (number % 10) * 100
number = number // 10

reversed_number += (number % 10) * 10
number = number // 10

reversed_number += number % 10

print("Перевернутое число:", reversed_number)
