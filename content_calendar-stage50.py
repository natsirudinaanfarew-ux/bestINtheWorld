# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: ContentCalendar
def print_status_report():
    """Выводит отчёт о статусе всех публикаций."""
    for pub in publications:
        print(f"  #{pub.id:03d} | {pub.status:20s} | {pub.channel:20s} | {pub.title:30s} | {pub.created_at}")
