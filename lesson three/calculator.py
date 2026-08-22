a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

operation = (input("Введіть дію(+, -, /, *): "))

if operation == '+':
    result = a + b
    print(f"Ваша відповідь: {result}")

elif operation == '-':
    result = a - b
    print(f"Ваша відповідь: {result}")

elif operation == '*':
    result = a * b
    print(f"Ваша відповідь: {result}")

elif operation == '/':
    result = a / b
    print(f"Ваша відповідь: {result}")

else:
    print("Помилка!")