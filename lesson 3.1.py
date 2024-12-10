num_1 = float(input("Введите первое число: "))
num_2 = float(input("Введите второе число: "))
operation = input("Введите действие(+, -, *, /): ")
if operation.strip() == "+":
    result = num_1 + num_2
    print("Результат:", result)
elif operation.strip() == "-":
    result = num_1 - num_2
    print("Результат:", result)
elif operation.strip() == "*":
    result = num_1 * num_2
    print("Результат:", result)
elif operation.strip() == "/":
    if num_2 == 0:
        print("Невозможно выполнить операцию")
    else:
        result = num_1 / num_2
        print("Результат:", result)
else:
    print("Неподдерживаемая операция")



