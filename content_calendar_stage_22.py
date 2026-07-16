# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: ContentCalendar
def check_overdue_reminders():
    """Выводит просроченные напоминания (статус == 'reminded', дата < сегодня)."""
    today = datetime.date.today()
    overdue = []
    for pub in publications:
        if pub.status == "reminded" and pub.date_remind < today:
            overdue.append(pub)
    return overdue
