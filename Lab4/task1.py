import json
def task(file_path: str) -> float:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Вычисление суммы произведений
    total = sum(item["score"] * item["weight"] for item in data)
    return round(total, 3) #округляем до 3 знаков после запятой
# Путь к JSON файлу
file_path = 'input.json'
# Вывод результата
print(task(file_path))