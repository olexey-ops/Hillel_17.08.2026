def move_zeros(nums):
    result = [x for x in nums if x != 0]
    result += [0] * (len(nums) - len(result))
    return result


# Перевірка на прикладах
tests = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0],
]

for t in tests:
    print(f"{t} -> {move_zeros(t)}")