from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum


def write(path, text):
    path.write_text(text, encoding="utf-8")


def expect_value_error(path, text, expected_substr=None):
    write(path, text)
    try:
        read_matrix(path)
    except ValueError as e:
        if expected_substr and expected_substr not in str(e):
            assert False, f"Ожидалась подстрока '{expected_substr}', получено: {e}"
        return
    assert False, "Ошибка не обнаружена"


def expect_file_not_found():
    bad = Path("/tmp/this_file_does_not_exist_12345.txt")
    try:
        read_matrix(bad)
    except FileNotFoundError:
        return
    assert False, "FileNotFoundError не обнаружен"


with TemporaryDirectory() as directory:
    d = Path(directory)

    # 1. Нормальный случай 1x1
    p = d / "ok_1x1.txt"
    write(p, "1 1\n0\n")
    assert read_matrix(p) == [[0]], "Тест 1x1 с нулём"

    # 2. Пустой файл
    p = d / "empty.txt"
    write(p, "")
    expect_value_error(p, "", "пуст")

    # 3. Заголовок 0 3
    p = d / "zero_rows.txt"
    expect_value_error(p, "0 3\n", "положительными")

    # 4. Заголовок 1 2, но строка 1 пустая (неверное количество чисел)
    p = d / "bad_count.txt"
    expect_value_error(p, "1 2\n7\n", "Строка 2")

    # 5. Заголовок 1 2, строка 1 содержит 'x'
    p = d / "non_numeric.txt"
    expect_value_error(p, "1 2\nx 5\n", "Строка 2")

    # 6. Заголовок 1 1, но две строки данных
    p = d / "extra_line.txt"
    expect_value_error(p, "1 1\n7\n8\n", "Ожидалось 1 строк")

    # 7. Отсутствующий путь
    expect_file_not_found()

    # 8. Контрольная матрица из задания
    p = d / "control.txt"
    write(p, "2 3\n1 -2 3\n4 0 -6\n")
    matrix = read_matrix(p)
    assert matrix == [[1, -2, 3], [4, 0, -6]], "Контрольная матрица"
    assert selected_sum(matrix) == 2, "Вариант 7: сумма элементов [-2, 3]"

print("Все проверки пройдены ")