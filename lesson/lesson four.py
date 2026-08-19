price = float(input("Введіть ціну: "))
vat_rate = float(input("Введіть %: "))
final_price = price + (price * vat_rate / 100)
print(f"Ціна: {final_price}")