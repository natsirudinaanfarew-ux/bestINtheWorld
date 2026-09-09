# === Stage 45: Добавь восстановление из резервной копии ===
# Project: ContentCalendar
import json, os, datetime, shutil

def load_backup(source, target):
    """Restore ContentCalendar state from a JSON backup file."""
    if not os.path.isfile(source):
        print(f"Error: backup file not found: {source}")
        return None
    try:
        with open(source, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error: corrupt backup file: {e}")
        return None
    if not isinstance(data, dict):
        print("Error: backup must be a JSON object")
        return None
    if not os.path.exists(target):
        os.makedirs(target)
    for item in data:
        if os.path.isfile(os.path.join(target, item)):
            shutil.copy2(os.path.join(target, item), os.path.join(source, item))
        else:
            shutil.copy2(os.path.join(source, item), os.path.join(target, item))
    print(f"Backup restored from: {source}")
    return data
