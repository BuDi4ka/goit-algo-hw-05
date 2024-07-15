from typing import Callable
import re


text_check = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b|\b\d+\b'
    for matches in re.findall(pattern, text):
        yield float(matches)


def sum_profit(text: str, func: Callable):
    return sum(func(text))
    

total_income = sum_profit(text_check, generator_numbers)
print(f"Загальний дохід: {total_income}")
