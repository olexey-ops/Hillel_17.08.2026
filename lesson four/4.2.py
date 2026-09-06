def sum_even_indices_times_last(arr):
    if not arr:
        return 0
    even_sum = sum(arr[i] for i in range(0, len(arr), 2))
    return even_sum * arr[-1]


# Перевірка на прикладах
tests = [
    [0, 1, 7, 2, 4, 8],
    [1, 3, 5],
    [6],
    [],
]

for t in tests:
    print(f"{t} => {sum_even_indices_times_last(t)}")