import string
import keyword

def is_valid_variable_name(s: str) -> bool:
    if not s:
        return False

    # не повинно починатися з цифри
    if s[0].isdigit():
        return False

    # не повинно містити великих літер
    if any(c.isupper() for c in s):
        return False

    # не повинно містити пробілів і пунктуації (окрім "_")
    forbidden = set(string.punctuation) - {'_'}
    forbidden.add(' ')
    if any(c in forbidden for c in s):
        return False

    # не повинно містити "__" підряд
    if '__' in s:
        return False

    # не повинно бути зареєстрованим словом
    if keyword.iskeyword(s):
        return False

    return True


if __name__ == "__main__":
    name = input()
    print(is_valid_variable_name(name))