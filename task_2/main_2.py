
import re
from typing import Callable

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    # Використовуємо регулярний вираз pattern для знаходження всіх дійсних чисел у тексті
    pattern = r"\d+.\d+"  
    for match in re.finditer(pattern, text): # Повертає ітератор для всіх неперекриваючих збігів у рядку. Для кожного збігу ітератор повертає об’єкт Match
        print(f"Дійсне число {float(match.group())}")
        yield float(match.group())  # Повертаємо дійсне число як результат
        
def sum_profit(text: str, func: Callable):
    total = sum(func(text)) # Викликаємо generator_numbers та підсумовуємо всі числа, що повертає генератор
    return total

if __name__ == "__main__":
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

