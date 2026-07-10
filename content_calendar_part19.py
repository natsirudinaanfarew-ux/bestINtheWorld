# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: ContentCalendar
def archive_records(records, cutoff=None):
    """Archive completed or old records. Returns a list of archived entries and the remaining active ones."""
    if cutoff is None:
        cutoff = datetime.now() - timedelta(days=30)
    
    archived = []
    active = []
    
    for record in records:
        status = record.get('status', '')
        created_at = record.get('created_at')
        
        if status == 'completed' or (created_at and created_at < cutoff):
            archive_entry = {**record, 'archived': True, 'archive_date': datetime.now().isoformat()}
            archived.append(archive_entry)
        else:
            active.append(record)
    
    return archived, active
