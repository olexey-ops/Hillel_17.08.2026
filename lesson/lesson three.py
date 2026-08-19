seconds = int(input("Введіть кількість секунд: "))
hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
final_seconds = remaining % 60
print(f"{hours} год {minutes} хв {final_seconds} сек")