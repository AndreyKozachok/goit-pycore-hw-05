import re
from typing import Callable

# Без використання циклу та yield.
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    numbers = list(map(float, re.findall(r"\d+.\d+", text))) # використовуємо регулярний вираз для знаходження дійсних чисел
    print(text)
    print(f"Всі дійсні числа {numbers}")
    return numbers
     
def sum_profit(text: str, func: Callable):
    profit = sum(func(text)) # викликаємо generator_numbers, сумуємо всі дійсні числа
    return profit


if __name__ == "__main__":

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")




