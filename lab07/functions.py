def sum_digits(number: int) -> int:
    number = abs(number)
    if number == 0:
        return 0
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def average(numbers: list) -> int:
    numbers = sum(numbers) / len(numbers)
    if numbers == 0:
        print("Список пуст")
    return numbers

def normalize_text(text: str) -> str:
    text = " ".join(text.lower().split())
    return text

def select_numbers(numbers: list, threshold: int)-> list:
    return [num for num in numbers if num != threshold]

