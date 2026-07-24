# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: ContentCalendar
def demo():
    print("=== ContentCalendar Demo ===")
    for pub in posts:
        print(f"  [{pub.channel}] {pub.title} — {pub.status}")
    print(f"\nИдеи ({len(ideas)}):")
    for i, idea in enumerate(ideas[:5], 1):
        print(f"  {i}. {idea.text}")
