# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: ContentCalendar
class ContentCalendar:
    def __init__(self):
        self.channels = {}
        self.topics = {}
        self.statuses = ["draft", "scheduled", "published"]
        self.ideas = []
    
    def validate_channel_name(self, name):
        if not isinstance(name, str) or len(name.strip()) < 2:
            return False, "Имя канала должно быть строкой длиной от 2 символов."
        return True, ""

    def validate_topic_name(self, name):
        if not isinstance(name, str) or len(name.strip()) < 3:
            return False, "Тема должна быть строкой длиной не менее 3 символов."
        return True, ""

    def validate_status(self, status):
        valid_statuses = self.statuses.copy()
        if status not in valid_statuses:
            return False, f"Статус должен быть одним из: {', '.join(valid_statuses)}."
        return True, ""

    def add_channel(self, name, description=""):
        is_valid, message = self.validate_channel_name(name)
        if not is_valid:
            print(message)
            return None
        self.channels[name] = {"description": description}
        return self.channels[name]

    def add_topic(self, name):
        is_valid, message = self.validate_topic_name(name)
        if not is_valid:
            print(message)
            return None
        self.topics[name] = []
        return self.topics[name]

    def set_status(self, status):
        is_valid, message = self.validate_status(status)
        if not is_valid:
            print(message)
            return False
        self.statuses.append(status)
        return True
