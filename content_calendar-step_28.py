# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: ContentCalendar
def print_project_metrics():
    total_posts = len(posts)
    unique_channels = len(set(p.channel for p in posts)) if posts else 0
    topic_counts = {}
    status_counts = {}
    for p in posts:
        topic_counts[p.topic] = topic_counts.get(p.topic, 0) + 1
        status_counts[p.status] = status_counts.get(p.status, 0) + 1

    print(f"Total posts: {total_posts}")
    print(f"Unique channels: {unique_channels}")
    print("Posts by topic:")
    for topic, count in sorted(topic_counts.items(), key=lambda x: -x[1]):
        print(f"  {topic}: {count}")
    print("Posts by status:")
    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count}")

print_project_metrics()
