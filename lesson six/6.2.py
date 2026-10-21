seconds = int(input())

days, rest = divmod(seconds, 24 * 60 * 60)
hours, rest = divmod(rest, 60 * 60)
minutes, secs = divmod(rest, 60)

if 11 <= days % 100 <= 14:
    word = "днів"
elif days % 10 == 1:
    word = "день"
elif 2 <= days % 10 <= 4:
    word = "дні"
else:
    word = "днів"

print(f"{days} {word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(secs).zfill(2)}