while True:
    try:
        a = float(input("Первое число: "))
        op = input("Операция (+, -, *, /): ")
        b = float(input("Второе число: "))
    except ValueError:
        print("Это не число, попробуйте ещё раз.\n")
        continue

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("На ноль делить нельзя.\n")
            continue
        result = a / b
    else:
        print("Неизвестная операция.\n")
        continue

    print(f"Результат: {result}\n")

    if input("Ещё раз? (да/нет): ").lower() != "да":
        break