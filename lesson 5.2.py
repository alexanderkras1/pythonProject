while True:
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))
    operation = input("Введите действие (+, -, *, /): ").strip()


    if operation == "+":
        result = num_1 + num_2
        print("Результат:", result)
    elif operation == "-":
        result = num_1 - num_2
        print("Результат:", result)
    elif operation == "*":
        result = num_1 * num_2
        print("Результат:", result)
    elif operation == "/":
        if num_2 == 0:
            print("Невозможно выполнить операцию: деление на ноль")
        else:
            result = num_1 / num_2
            print("Результат:", result)
    else:
        print("Неподдерживаемая операция")

    user_answer = input("Продолжить? (yes/no): ").strip()
    if user_answer != "yes":
        print("Калькулятор завершает работу.")
        break

