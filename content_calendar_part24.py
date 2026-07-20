# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: ContentCalendar
def print_post_detail(post):
    if not post:
        return
    print(f"=== {post['title']} ===")
    for k, v in post.items():
        if isinstance(v, (list, dict)):
            continue
        print(f"{k}: {v}")
