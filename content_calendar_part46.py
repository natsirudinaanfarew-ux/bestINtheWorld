# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: ContentCalendar
# Миграция структуры данных: добавление версии и истории изменений
MIGRATION_VERSION = 46

def migrate_structure():
    """Применяет миграцию версии 46: добавляет поля 'history' и 'migration_log' к корневому объекту."""
    global MIGRATION_VERSION
    MIGRATION_VERSION += 1

    # Создаём контейнер для истории изменений
    history = {
        "versions": [],
        "current_version": MIGRATION_VERSION,
        "migration_log": []
    }

    # Записываем текущую версию в историю
    history["versions"].append({
        "version": MIGRATION_VERSION,
        "timestamp": datetime.now().isoformat(),
        "description": "Добавлена структура миграции для отслеживания изменений в контент-календаре"
    })

    # Логирование миграции
    history["migration_log"].append({
        "action": "add_migration",
        "from_version": MIGRATION_VERSION - 1,
        "to_version": MIGRATION_VERSION,
        "details": "Добавлена поддержка версионирования структуры данных"
    })

    return history
