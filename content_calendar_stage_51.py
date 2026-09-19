# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: ContentCalendar
class DataLog:
    def __init__(self):
        self._log = []

    def log(self, action, record, timestamp=None):
        if timestamp is None:
            import datetime
            timestamp = datetime.datetime.now().isoformat()
        self._log.append({"action": action, "record": record, "timestamp": timestamp})

    def get_history(self):
        return self._log
