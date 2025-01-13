num = int(input("Введите ваше число: "))

str(num)

digits = [int(digit) for digit in str(num)]
print(digits)

result = 1
for digit in digits:
    result *= digit
print(result)

while num >= 10:
    digits = [int(digit) for digit in str(num)]
    result = 1
    for digit in digits:
        result *= digit
    num = result

print(f"Итоговое число: {num}")

