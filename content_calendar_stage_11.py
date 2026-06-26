# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: ContentCalendar
import json, os, sys
DATA_FILE = "content_calendar.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"channels": [], "topics": [], "posts": [], "ideas": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Ошибка чтения файла данных. Создание нового.")
        return {"channels": [], "topics": [], "posts": [], "ideas": []}

def save_data(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"Ошибка сохранения данных: {e}")
        return False

def get_data():
    data = load_data()
    # Добавляем текущую сессию в память приложения (если используется глобальный словарь или класс)
    if not hasattr(sys.modules[__name__], '_current_session'):
        sys.modules[__name__]._current_session = data
    return sys.modules[__name__]._current_session

def update_data(update_func):
    current = get_data()
    updated = update_func(current.copy()) # Копируем, чтобы не мутировать исходный при чтении
    if save_data(updated):
        sys.modules[__name__]._current_session = updated
        return True
    return False

# Пример использования для сохранения списка каналов:
# channels = get_data()["channels"]
# update_data(lambda d: {"channels": d["channels"] + [{"id": 1, "name": "Новый канал"}]})
