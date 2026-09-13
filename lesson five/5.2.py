def calculator():
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    while True:
        try:
            a = float(input("Введіть перше число: "))
            op = input("Введіть операцію (+, -, *, /): ").strip()
            b = float(input("Введіть друге число: "))

            if op not in operations:
                print("Невідома операція!")
            elif op == '/' and b == 0:
                print("Ділення на нуль неможливе!")
            else:
                result = operations[op](a, b)
                print(f"Результат: {result}")

        except ValueError:
            print("Помилка: введіть коректне число!")

        answer = input("Продовжити роботу калькулятора? (yes/y - так, будь-що інше - ні): ").strip().lower()
        if answer not in ('yes', 'y'):
            print("Роботу калькулятора завершено.")
            break


if __name__ == "__main__":
    calculator()