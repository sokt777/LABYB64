def read_matrix(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file]

    # Удаляем один допустимый пустой перевод строки в конце
    if lines and lines[-1] == "":
        lines = lines[:-1]

    if not lines:
        raise ValueError("Файл пуст")

    # Заголовок
    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Строка 1: ожидалось два числа (rows columns)")
    try:
        rows, columns = int(header[0]), int(header[1])
    except ValueError:
        raise ValueError("Строка 1: заголовок должен содержать целые числа")
    if rows <= 0 or columns <= 0:
        raise ValueError("Строка 1: размеры должны быть положительными")

    if len(lines) - 1 != rows:
        raise ValueError(
            f"Ожидалось {rows} строк данных, получено {len(lines) - 1}"
        )

    matrix = []
    for i in range(rows):
        line_num = i + 2
        parts = lines[i + 1].split()
        if len(parts) != columns:
            raise ValueError(
                f"Строка {line_num}: ожидалось {columns} чисел, "
                f"получено {len(parts)}"
            )
        row = []
        for part in parts:
            try:
                row.append(int(part))
            except ValueError:
                raise ValueError(
                    f"Строка {line_num}: нечисловая ячейка '{part}'"
                )
        matrix.append(row)

    return matrix

def selected_sum(matrix):

    total = 0
    for row in matrix:
        for value in row:
            if -2 <= value <= 3:
                total += value
    return total