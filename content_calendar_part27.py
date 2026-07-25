# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: ContentCalendar
def reset_demo_data():
    """Сбросить все демо-данные к начальным значениям."""
    channels = [
        {"id": "ch1", "name": "Блог", "description": "Технические статьи"},
        {"id": "ch2", "name": "Twitter", "description": "Короткие мысли и новости"},
        {"id": "ch3", "name": "YouTube", "description": "Видео-обзоры и туториалы"},
    ]
    topics = ["Python", "AI/ML", "DevOps", "Дизайн", "Маркетинг"]
    statuses = [
        {"id": "s1", "name": "Идея", "color": "#e0e0e0"},
        {"id": "s2", "name": "Черновик", "color": "#bbdefb"},
        {"id": "s3", "name": "В работе", "color": "#ffcc80"},
        {"id": "s4", "name": "Готово", "color": "#c8e6c9"},
    ]
    ideas = [
        {"title": "Как работает генеративная модель? Обзор GPT-4", "channel_id": "ch3"},
        {"title": "10 советов по оптимизации Python кода", "channel_id": "ch1"},
        {"title": "Новый тренд в UI/UX дизайне 2025", "channel_id": "ch2"},
    ]
    posts = [
        {
            "id": "p1",
            "title": "Введение в Data Science с Python",
            "status_id": "s4",
            "channel_id": "ch1",
            "topic_ids": ["Python"],
            "publish_date": "2025-06-15",
            "views": 1200,
        },
    ]
    return channels, topics, statuses, ideas, posts

def clear_state():
    """Полностью очистить все данные (для тестирования)."""
    return [], [], [], [], []
