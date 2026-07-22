# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: ContentCalendar
def validate_date(date_str):
    """Парсинг даты в форматах YYYY-MM-DD, DD.MM.YYYY, DD/MM/YYYY."""
    import datetime as dt
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
        try:
            return dt.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Некорректная дата '{date_str}'. Используйте формат YYYY-MM-DD или DD.MM.YYYY")

def format_date(dt_obj):
    """Форматирование даты в YYYY-MM-DD."""
    return dt_obj.strftime("%Y-%m-%d") if isinstance(dt_obj, dt.datetime) else dt_obj.isoformat()
