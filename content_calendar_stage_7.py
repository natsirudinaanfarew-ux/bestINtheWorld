# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: ContentCalendar
def sort_content_items(items, key='date', reverse=False):
    if not items: return []
    mapping = {'date': lambda x: x.get('publish_date') or x.get('created_at'), 'priority': lambda x: -x.get('priority', 0), 'name': str}
    sort_key = mapping.get(key, mapping['date'])
    sorted_items = sorted(items, key=sort_key, reverse=(key == 'priority' and not reverse))
    if key == 'name': return sorted_items
    return sorted_items
