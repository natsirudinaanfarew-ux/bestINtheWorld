# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: ContentCalendar
def edit_post(post_id: int, updates: dict) -> Optional[Post]:
    """Редактирует запись по ID, возвращая обновлённый объект или None."""
    for post in posts:
        if post.id == post_id:
            # Обновляем только предоставленные поля, сохраняя остальные без изменений
            for key, value in updates.items():
                if hasattr(post, key):
                    setattr(post, key, value)
            return post
    print(f"Запись с ID {post_id} не найдена.")
    return None
