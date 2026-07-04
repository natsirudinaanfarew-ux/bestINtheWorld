# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: ContentCalendar
def calculate_monthly_stats(posts):
    from collections import defaultdict
    stats = defaultdict(lambda: {'total': 0, 'published': 0})
    for post in posts:
        if not isinstance(post['date'], str) or len(post['date']) < 7: continue
        month_key = f"{post['date'][:4]}-{post['date'][5:7]}"
        stats[month_key]['total'] += 1
        if post.get('status') == 'published':
            stats[month_key]['published'] += 1
    return dict(sorted(stats.items()))
