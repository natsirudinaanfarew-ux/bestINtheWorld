# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: ContentCalendar
def import_from_text(filepath):
    """Import publications from simple text format:
    date|channel|topic|status|idea
    """
    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('|')
            if len(parts) != 5:
                continue
            date_str, channel, topic, status, idea = parts
            records.append({
                'date': date_str,
                'channel': channel.strip(),
                'topic': topic.strip(),
                'status': status.strip(),
                'idea': idea.strip()
            })
    return records

def export_to_text(filepath, records):
    """Export records to simple text format."""
    with open(filepath, 'w', encoding='utf-8') as f:
        for r in records:
            f.write(f"{r['date']}|{r['channel']}|{r['topic']}|{r['status']}|{r['idea']}\n")

def print_report(records):
    """Print a simple text report of publications."""
    total = len(records)
    by_status = {}
    for r in records:
        s = r['status']
        by_status[s] = by_status.get(s, 0) + 1
    print(f"Total publications: {total}")
    print("By status:")
    for s, count in sorted(by_status.items()):
        print(f"  {s}: {count}")
    by_channel = {}
    for r in records:
        c = r['channel']
        by_channel[c] = by_channel.get(c, 0) + 1
    print("By channel:")
    for c, count in sorted(by_channel.items()):
        print(f"  {c}: {count}")

if __name__ == '__main__':
    sample = [
        {'date': '2024-01-15', 'channel': 'Twitter', 'topic': 'Python Tips', 'status': 'published', 'idea': 'New feature demo'},
        {'date': '2024-01-16', 'channel': 'Blog', 'topic': 'Tutorial', 'status': 'draft', 'idea': 'Step-by-step guide'},
        {'date': '2024-01-17', 'channel': 'Twitter', 'topic': 'Python Tips', 'status': 'published', 'idea': 'Quick win'},
    ]
    export_to_text('export.txt', sample)
    imported = import_from_text('export.txt')
    print_report(imported)
