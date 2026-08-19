number = int(input("Введіть число: "))
git_sum = sum(int(digit) for digit in str(abs(number)))
print(f"Сума цифр: {git_sum}")