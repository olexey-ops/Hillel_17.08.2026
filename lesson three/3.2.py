def move_last_to_front(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + lst[:-1]


# Перевірка на прикладах
print(move_last_to_front([12, 3, 4, 10]))       # [10, 12, 3, 4]
print(move_last_to_front([1]))                  # [1]
print(move_last_to_front([]))                   # []
print(move_last_to_front([12, 3, 4, 10, 8]))    # [8, 12, 3, 4, 10]