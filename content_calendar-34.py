# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: ContentCalendar
class ContentTemplate:
    def __init__(self, name, channels=None, topics=None, statuses=None):
        self.name = name
        self.channels = channels or []
        self.topics = topics or []
        self.statuses = statuses or ["draft"]

    def create_post(self, title, body):
        return {
            "title": title,
            "body": body,
            "channels": list(self.channels),
            "topics": list(self.topics),
            "status": self.statuses[0] if self.statuses else "draft",
            "created_at": datetime.now().isoformat(),
        }

    def __repr__(self):
        return f"<ContentTemplate: {self.name}>"
