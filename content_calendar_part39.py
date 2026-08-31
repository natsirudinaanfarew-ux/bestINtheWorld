# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: ContentCalendar
class ContentCalendar:
    def __init__(self):
        self.publications = []
        self.channels = []
        self.themes = []
        self.statuses = []
        self.ideas = []

    def add_publication(self, title, channel, theme, status, date, content, idea=None):
        if channel not in self.channels:
            self.channels.append(channel)
        if theme not in self.themes:
            self.themes.append(theme)
        if status not in self.statuses:
            self.statuses.append(status)
        if idea is not None and idea not in self.ideas:
            self.ideas.append(idea)
        self.publications.append({
            "title": title,
            "channel": channel,
            "theme": theme,
            "status": status,
            "date": date,
            "content": content,
            "idea": idea
        })
        return self.publications[-1]

    def add_channel(self, name):
        if name not in self.channels:
            self.channels.append(name)
        return self.channels[-1]

    def add_theme(self, name):
        if name not in self.themes:
            self.themes.append(name)
        return self.themes[-1]

    def add_status(self, name):
        if name not in self.statuses:
            self.statuses.append(name)
        return self.statuses[-1]

    def add_idea(self, text):
        if text not in self.ideas:
            self.ideas.append(text)
        return self.ideas[-1]

    def get_publications(self, channel=None, theme=None, status=None):
        filtered = self.publications
        if channel:
            filtered = [p for p in filtered if p["channel"] == channel]
        if theme:
            filtered = [p for p in filtered if p["theme"] == theme]
        if status:
            filtered = [p for p in filtered if p["status"] == status]
        return filtered

    def get_channels(self):
        return self.channels

    def get_themes(self):
        return self.themes

    def get_statuses(self):
        return self.statuses

    def get_ideas(self):
        return self.ideas

    def get_statistics(self):
        return {
            "total_publications": len(self.publications),
            "total_channels": len(self.channels),
            "total_themes": len(self.themes),
            "total_statuses": len(self.statuses),
            "total_ideas": len(self.ideas)
        }

    def get_schedule(self, days=30):
        from datetime import datetime, timedelta
        today = datetime.now().date()
        schedule = []
        for i in range(days):
            day = today + timedelta(days=i)
            day_str = day.strftime("%Y-%m-%d")
            day_publications = [p for p in self.publications if p["date"] == day_str]
            if day_publications:
                schedule.append({
                    "date": day_str,
                    "publications": day_publications
                })
        return schedule

    def get_overview(self):
        overview = {
            "channels": self.channels,
            "themes": self.themes,
            "statuses": self.statuses,
            "ideas": self.ideas,
            "publications": self.publications,
            "statistics": self.get_statistics()
        }
        return overview

    def get_usage_scenarios(self):
        return [
            "Добавить канал, тему и статус",
            "Добавить идею",
            "Добавить публикацию",
            "Отобразить все публикации",
            "Получить расписание на N дней",
            "Получить обзор"
        ]
