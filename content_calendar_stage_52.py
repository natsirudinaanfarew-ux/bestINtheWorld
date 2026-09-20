# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: ContentCalendar
def export_report(campaigns):
    """Экспортирует краткий текстовый отчёт по всем кампаниям."""
    lines = ["=== ContentCalendar Report ===", f"Generated: {datetime.now():%Y-%m-%d %H:%M}"]
    for camp in campaigns:
        lines.append(f"\n--- {camp['name']} ---")
        lines.append(f"  Status: {camp['status']}")
        lines.append(f"  Channels: {', '.join(ch['name'] for ch in camp['channels'])}")
        lines.append(f"  Topics: {', '.join(t['name'] for t in camp['topics'])}")
        lines.append(f"  Ideas: {camp['ideas_count']}")
        lines.append(f"  Posts: {camp['posts_count']}")
    return "\n".join(lines)
