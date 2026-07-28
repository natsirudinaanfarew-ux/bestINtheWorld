# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: ContentCalendar
def configure_app(settings: dict) -> App:
    """Create an App instance using a configuration dictionary."""
    channels = settings.get("channels", [])
    topics = settings.get("topics", [])
    statuses = settings.get("statuses", ["draft", "scheduled", "published"])
    ideas = settings.get("ideas", [])

    app = App()
    for ch in channels:
        app.add_channel(ch)
    for topic in topics:
        app.add_topic(topic)
    app.set_status_list(statuses)
    for idea in ideas:
        app.add_idea(idea)
    return app
