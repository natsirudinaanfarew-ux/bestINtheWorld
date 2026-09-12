# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: ContentCalendar
def demo():
    print("=== ContentCalendar Demo ===")
    
    # Создаем каналы
    channels = [
        {"name": "Telegram", "platform": "telegram"},
        {"name": "YouTube", "platform": "youtube"},
        {"name": "Twitter", "platform": "twitter"},
    ]
    print(f"Добавлено {len(channels)} каналов")
    
    # Создаем темы
    topics = ["Python", "AI", "WebDev", "Мотивация"]
    print(f"Добавлено {len(topics)} тем")
    
    # Создаем статусы
    statuses = ["idea", "draft", "scheduled", "published", "failed"]
    print(f"Добавлено {len(statuses)} статусов")
    
    # Добавляем идеи
    ideas = [
        {"title": "Как начать изучать Python", "topic": "Python", "status": "idea"},
        {"title": "Промт-инжиниринг для начинающих", "topic": "AI", "status": "idea"},
        {"title": "Создание REST API с нуля", "topic": "WebDev", "status": "idea"},
    ]
    print(f"Добавлено {len(ideas)} идей")
    
    # Превращаем идеи в черновики
    drafts = []
    for idea in ideas:
        drafts.append({"title": idea["title"], "topic": idea["topic"], "status": "draft"})
        idea["status"] = "draft"
    print(f"Превращено {len(drafts)} идей в черновики")
    
    # Публикуем один черновик
    published = [d for d in drafts if d["status"] == "draft"]
    if published:
        published[0]["status"] = "published"
    print(f"Опубликовано {len(published)} публикаций")
    
    # Устанавливаем расписание
    scheduled = [d for d in drafts if d["status"] == "draft"]
    if scheduled:
        scheduled[0]["status"] = "scheduled"
    print(f"Запланировано {len(scheduled)} публикаций")
    
    print("\n=== Демонстрация завершена ===")
