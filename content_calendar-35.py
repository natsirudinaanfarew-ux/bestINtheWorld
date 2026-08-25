# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: ContentCalendar
def get_next_actions(calendar):
    """Рекомендует следующие действия на основе текущего состояния календаря."""
    if not calendar.publications:
        return ["Создайте первую публикацию"]
    
    channels = calendar.channels
    themes = calendar.themes
    statuses = calendar.statuses
    ideas = calendar.ideas
    
    next_actions = []
    
    if ideas and not any(pub.uses_idea for pub in calendar.publications):
        next_actions.append("Используйте хотя бы одну идею из списка идей")
    
    if calendar.statuses:
        for status in calendar.statuses:
            if status.name == "draft":
                if not any(pub.status == "draft" for pub in calendar.publications):
                    next_actions.append("Напишите черновик публикации")
                elif not any(pub.status == "scheduled" for pub in calendar.publications):
                    next_actions.append("Запланируйте хотя бы одну публикацию")
                elif not any(pub.status == "published" for pub in calendar.publications):
                    next_actions.append("Опубликуйте хотя бы одну публикацию")
    
    if calendar.channels and not any(pub.channel_id in channels for pub in calendar.publications):
        next_actions.append("Привяжите публикации к существующим каналам")
    
    if calendar.themes and not any(pub.topics in themes for pub in calendar.publications):
        next_actions.append("Добавьте темы к публикациям")
    
    if not next_actions:
        next_actions.append("Все действия выполнены, поздравляю!")
    
    return next_actions
