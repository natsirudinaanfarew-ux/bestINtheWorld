# === Stage 43: Добавь пагинацию длинных списков ===
# Project: ContentCalendar
def paginate(items, page_size=10, page=0):
    """Compact pagination helper: returns (current_page_items, total_pages)."""
    if page < 0:
        page = 0
    total_pages = max(1, (len(items) + page_size - 1) // page_size)
    start = page * page_size
    end = start + page_size
    return items[start:end], total_pages
