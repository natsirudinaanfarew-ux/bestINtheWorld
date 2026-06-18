# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: ContentCalendar
def filter_posts(status=None, category=None, tags=None):
    filtered = []
    for post in posts:
        if status and post['status'] != status:
            continue
        if category and post.get('category') != category:
            continue
        if tags:
            post_tags = set(post.get('tags', []))
            if not any(tag in post_tags for tag in tags):
                continue
        filtered.append(post)
    return filtered

def search_posts(query=None, limit=10):
    results = []
    query_lower = query.lower() if query else ''
    for post in posts:
        text = f"{post.get('title', '')} {post.get('content', '')}".lower()
        tags_str = ' '.join(post.get('tags', [])).lower()
        if query_lower and query_lower not in text and query_lower not in tags_str:
            continue
        results.append(post)
    return results[:limit]
