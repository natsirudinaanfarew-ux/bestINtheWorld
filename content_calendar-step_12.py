# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: ContentCalendar
import json, os

def load_data(filepath: str) -> dict | None:
    if not os.path.exists(filepath):
        print(f"Файл {filepath} не найден.")
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict) and all(k in data for k in ['posts', 'channels']):
            print("Данные успешно загружены.")
            return data
        else:
            raise ValueError("Неверная структура JSON")
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
    except Exception as e:
        print(f"Произошла неизвестная ошибка при чтении файла: {e}")
    return None
