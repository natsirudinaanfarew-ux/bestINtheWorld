# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: ContentCalendar
def generate_summary(calendar):
    if not calendar:
        return "Календарь пуст."
    
    posts = calendar.get("posts", [])
    channels = calendar.get("channels", [])
    themes = calendar.get("themes", [])
    statuses = set(p["status"] for p in posts)
    
    summary_lines = [f"Сводка по календарю: {len(posts)} публикаций, {len(channels)} каналов."]
    
    if channels:
        channel_names = ", ".join(c["name"] for c in channels[:3]) + (" и др." if len(channels) > 3 else "")
        summary_lines.append(f"Каналы: {channel_names}.")
    
    if themes:
        theme_names = ", ".join(t["name"] for t in themes[:5]) + ("..." if len(themes) > 5 else "")
        summary_lines.append(f"Темы: {theme_names}.")
        
    active_count = sum(1 for p in posts if p.get("status", "draft") == "published")
    draft_count = sum(1 for p in posts if p.get("status", "draft") != "published")
    
    summary_lines.append(f"Статусы: {active_count} опубликовано, {draft_count} в черновике.")
    
    ideas = calendar.get("ideas", [])
    if ideas:
        idea_topics = set(i["topic"] for i in ideas)
        summary_lines.append(f"Идей на разработку: {len(ideas)} ({', '.join(idea_topics[:3])}).")
        
    return "\n".join(summary_lines)
