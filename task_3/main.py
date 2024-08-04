
from pathlib import Path
import sys
import re


def parse_log_line(line: str) -> dict: # функція парсенгу рядків логу
    patern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$"
    match = re.match(patern, line)
    if match:
        return {
            "timestemp": match.group(1),
            "level": match.group(2),
            "message": match.group(3)
        }
    else:
        raise ValueError("Invalid log line format")


def load_logs(file_path: str) -> list: # функція для завантаження логів з файлу
    logs_list: list = []
    with open(file_path, "r") as file:
        for line in file:
            logs_list.append(parse_log_line(line.strip()))
    return logs_list


def filter_logs_by_level(logs: list, level: str) -> list: # функція для фільтрації логів за рівнем
    return [log for log in logs if log["level"] == level.upper()]
    

def count_logs_by_level(logs: list) -> dict: # функція для підрахункузаписів за рівнем логування
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict): # функція форматує та виводить результат
    print("Рівень логування | Кількість")
    print("_________________|__________")
    for level, count in counts.items():
        print(f"{level.upper():<17}| {count}")


def display_log_details(logs: list):
    print("\nДеталі логів для певного рівня ")
    for log in logs:
        print(f"{log["timestemp"]} - {log["message"]}")


def main():
    if len(sys.argv) < 2:
        print("Потрібно вказати шлях до файлу логів")
        return
    
    file_path = sys.argv[1]
    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print("Файл логів не знайдено")
        return
    except Exception as e:
        print(f"Помилка при читанні файлу логів: {e}")
        return
    
    # Обробка додаткового аргументу для фільтрації за рівнем логування
    if len(sys.argv) >= 3:
        level_filter = sys.argv[2]
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
    
        filtered_logs = filter_logs_by_level(logs, level_filter)
        display_log_details(filtered_logs)
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)


if __name__ == "__main__":
    main()
   
    
