# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: ContentCalendar
import os
import shutil
from datetime import datetime

def backup_data_file(data_file_path, backup_dir=".backups"):
    """Создаёт резервную копию файла данных в папке .backups с указанием даты."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(data_file_path)}.{timestamp}")
    shutil.copy2(data_file_path, backup_path)
    print(f"Резервная копия сохранена: {backup_path}")
    return backup_path
