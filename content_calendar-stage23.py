# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: ContentCalendar
def console_table(data, headers):
    col_widths = [len(h) for h in headers]
    for row in data:
        for i, cell in enumerate(row):
            if len(str(cell)) > col_widths[i]:
                col_widths[i] = len(str(cell))
    
    fmt_str = " | ".join(f"{{:<{col_widths[i]}}}" for i in range(len(headers)))
    print(fmt_str.format(*headers))
    print("-+-".join("-" * w for w in col_widths))
    for row in data:
        print(fmt_str.format(*[str(c) for c in row]))

def show_all():
    console_table(
        [list(p) for p in content_calendar],
        ["ID", "Title", "Channel", "Theme", "Status", "Date"]
    )
