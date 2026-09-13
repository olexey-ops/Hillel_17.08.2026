import string

def make_hashtag(s: str) -> str:
    # видаляємо всі символи пунктуації, замінюючи їх на пробіли
    cleaned = ''.join(' ' if c in string.punctuation else c for c in s)

    # розбиваємо на слова, кожне слово робимо з великої літери
    words = cleaned.split()
    hashtag = '#' + ''.join(word.capitalize() for word in words)

