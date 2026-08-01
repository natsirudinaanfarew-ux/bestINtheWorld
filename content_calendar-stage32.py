# === Stage 32: Добавь журнал действий пользователя ===
# Project: ContentCalendar
class ActionLog:
    def __init__(self):
        self._history = []

    def log(self, action_type: str, details: dict) -> None:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action_type": action_type,
            "details": details
        }
        self._history.append(entry)

    @property
    def history(self):
        return list(self._history)

    def clear(self) -> None:
        self._history.clear()

    def summary(self, top_n=5) -> list:
        counts = {}
        for entry in self._history:
            t = entry["action_type"]
            counts[t] = counts.get(t, 0) + 1
        return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:top_n]

    def __len__(self):
        return len(self._history)
