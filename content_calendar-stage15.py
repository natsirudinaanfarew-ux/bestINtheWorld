# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: ContentCalendar
def calculate_weekly_stats(published_posts):
    from datetime import date, timedelta
    if not published_posts: return {}
    min_date = min(post['date'] for post in published_posts)
    max_date = max(post['date'] for post in published_posts)
    current = min_date - timedelta(days=min_date.weekday())
    stats = {current + timedelta(weeks=i): 0 for i in range((max_date - current).days // 7 + 1)}
    for post in published_posts:
        week_start = (post['date'] - timedelta(days=post['date'].weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
        stats[week_start] += 1
    return {k.strftime('%Y-%m-%d'): v for k, v in sorted(stats.items())}
