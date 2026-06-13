# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: ContentCalendar
class ContentCalendar:
    def __init__(self):
        self._posts = []
        self._channels = {}
        self._topics = {}
        self._statuses = {"draft": "Черновик", "scheduled": "Запланировано", "published": "Опубликовано"}
    
    def add_channel(self, name: str, description: str):
        if not name or name in self._channels: return False
        self._channels[name] = {"name": name, "description": description}
        return True
    
    def add_topic(self, channel_name: str, topic_name: str):
        if channel_name not in self._channels: return False
        key = f"{channel_name}:{topic_name}"
        if key in self._topics: return False
        self._topics[key] = {"name": topic_name}
        return True
    
    def add_post(self, title: str, content: str, channel_name: str, 
                  topic_name: str, status: str = "draft", idea: str | None = None):
        if not all([title, content]): return False
        key = f"{channel_name}:{topic_name}"
        if key not in self._topics: return False
        post_id = len(self._posts) + 1
        self._posts.append({
            "id": post_id,
            "title": title,
            "content": content,
            "channel": channel_name,
            "topic": topic_name,
            "status": status,
            "idea": idea or ""
        })
        return True
    
    def get_posts(self, channel: str | None = None, status: str | None = None):
        result = self._posts.copy()
        if channel:
            filtered = [p for p in result if p["channel"] == channel]
            return filtered if filtered else []
        if status and status in self._statuses:
            filtered = [p for p in result if p["status"] == status]
            return filtered if filtered else []
        return result
    
    def get_channels(self):
        return list(self._channels.values())
    
    def get_topics_for_channel(self, channel_name: str):
        if channel_name not in self._channels: return []
        topics = [t for k, t in self._topics.items() if k.startswith(channel_name + ":")]
        return topics
