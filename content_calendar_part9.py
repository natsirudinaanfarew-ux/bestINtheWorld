# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: ContentCalendar
import json, sys
from datetime import datetime, timedelta
INITIAL_DATA = '''
{
  "channels": [
    {"id": 1, "name": "Telegram", "url": "https://t.me/channel"},
    {"id": 2, "name": "VKontakte", "url": "https://vk.com/public"}
  ],
  "topics": ["Python", "AI", "News"],
  "statuses": ["draft", "scheduled", "published"],
  "ideas": [
    {"text": "Как работает asyncio?", "channel_id": 1, "topic": "Python"},
    {"text": "Топ нейросетей 2024", "channel_id": 2, "topic": "AI"}
  ],
  "posts": []
}
'''

def load_initial_data():
    try:
        data = json.loads(INITIAL_DATA)
        now = datetime.now()
        
        # Генерация тестовых постов для демо-режима
        if not data["posts"]:
            for i, idea in enumerate(data["ideas"]):
                post_date = (now - timedelta(days=i)).date().isoformat()
                data["posts"].append({
                    "id": len(data["posts"]) + 1,
                    "text": idea["text"],
                    "channel_id": idea["channel_id"],
                    "topic": idea["topic"],
                    "status": "draft",
                    "date": post_date
                })
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON данных: {e}")
        sys.exit(1)

if __name__ == "__main__":
    calendar_data = load_initial_data()
    # Здесь можно сохранить данные в файл или использовать дальше
    # Пример сохранения в локальный JSON для последующих итераций
    with open("calendar_data.json", "w", encoding="utf-8") as f:
        json.dump(calendar_data, f, ensure_ascii=False, indent=2)
