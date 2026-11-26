from table import row_sums, column_sums, diagonal_pattern, transform


# --- row_sums ---
assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
assert row_sums([[7]]) == [7]
assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert row_sums([]) == []

# --- column_sums ---
assert column_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]
assert column_sums([[7]]) == [7]
assert column_sums([[1], [-1], [0]]) == [0]
assert column_sums([]) == []

# --- diagonal_pattern ---
assert diagonal_pattern(1) == [[0]]
assert diagonal_pattern(3) == [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0],
]

# --- transform (вариант 7: положительные +5) ---
control = [[-2, 0, 3], [4, -5, 6]]
expected_variant7 = [[-2, 0, 8], [9, -5, 11]]
assert transform(control) == expected_variant7
assert transform([]) == []

# Проверка: изменение результата не должно менять исходную матрицу
result = transform(control)
result[0][0] = 999
assert control == [[-2, 0, 3], [4, -5, 6]], "Исходная матрица изменилась!"

print("Все тесты пройдены ")