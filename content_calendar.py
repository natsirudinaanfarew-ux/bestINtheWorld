# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: ContentCalendar
def init_calendar():
    channels = ["Tech Blog", "Life Hacks", "News"]
    topics = ["Python", "AI", "Travel", "Health"]
    statuses = ["Draft", "Scheduled", "Published", "Cancelled"]
    
    posts = [
        {"id": 1, "channel": "Tech Blog", "topic": "Python", "title": "Async Basics", "status": "Draft", "idea": "Explain async/await simply"},
        {"id": 2, "channel": "Life Hacks", "topic": "Health", "title": "Morning Routine", "status": "Scheduled", "idea": "5 habits for energy"},
    ]
    
    ideas = [
        {"text": "Write a tutorial on list comprehensions", "priority": "high"},
        {"text": "Interview with a local developer", "priority": "medium"},
    ]
    
    return {
        "channels": channels,
        "topics": topics,
        "statuses": statuses,
        "posts": posts,
        "ideas": ideas
    }

if __name__ == "__main__":
    calendar = init_calendar()
    print(f"Channels: {calendar['channels']}")
    print(f"Total posts: {len(calendar['posts'])}")
