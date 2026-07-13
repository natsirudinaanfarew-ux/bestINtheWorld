# === Stage 20: Добавь восстановление записей из архива ===
# Project: ContentCalendar
def restore_from_archive():
    """Восстанавливает записи из резервной копии."""
    import os, json
    archive_path = "archive.json"
    if not os.path.exists(archive_path):
        print("Архив не найден.")
        return []
    with open(archive_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    records = data.get('records', [])
    for rec in records:
        if isinstance(rec, dict):
            for key in ['title', 'content', 'channel_id', 'status']:
                if key not in rec and key in rec.get('_archive_fields', {}):
                    rec[key] = rec['_archive_fields'][key]
    return records
