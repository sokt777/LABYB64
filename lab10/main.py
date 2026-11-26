rom pathlib import Path
from table import row_sums, column_sums
from files_lab import read_matrix, selected_sum


def read_positive_integer():
    """Повторяет ввод, пока не получит целое число больше нуля."""
    while True:
        raw = input("Введите целое число больше нуля: ")
        try:
            number = int(raw)
        except ValueError:
            print("Ошибка: не целое число")
            continue
        if number <= 0:
            print("Ошибка: должно быть больше нуля")
            continue
        return number


def main():
    folder = Path(__file__).resolve().parent
    source = folder / "matrix.txt"
    report = folder / "report.txt"

    # Задание 1: надёжный ввод размера
    print("--- Задание 1: надёжный ввод ---")
    size = read_positive_integer()
    print(f"Получено положительное целое: {size}\n")

    # Задание 2 и 3: чтение матрицы и отчёт
    print("--- Задание 2 и 3: чтение и отчёт ---")
    try:
        matrix = read_matrix(source)
    except FileNotFoundError:
        print(f"Файл не найден: {source}")
        return
    except ValueError as e:
        print(f"Ошибка формата: {e}")
        return
    except OSError as e:
        print(f"Ошибка доступа к файлу: {e}")
        return

    print("Матрица прочитана:")
    for row in matrix:
        print(*row)

    rs = row_sums(matrix)
    cs = column_sums(matrix)
    variant_sum = selected_sum(matrix)

    # Формируем отчёт в памяти, записываем только после успешной проверки
    report_lines = [
        f"Суммы строк: {' '.join(str(x) for x in rs)}",
        f"Суммы столбцов: {' '.join(str(x) for x in cs)}",
        f"Результат варианта: {variant_sum}",
    ]
    report_text = "\n".join(report_lines) + "\n"

    try:
        with open(report, "w", encoding="utf-8") as file:
            file.write(report_text)
        print(f"\nОтчёт записан в {report.name}")
    except OSError as e:
        print(f"Не удалось записать отчёт: {e}")


if __name__ == "__main__":
    main()