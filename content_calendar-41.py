# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: ContentCalendar
class DryRunError(Exception):
    """Raised when dry-run mode is active and an operation would modify data."""
    pass
