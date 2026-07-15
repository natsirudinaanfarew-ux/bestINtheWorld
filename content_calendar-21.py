# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: ContentCalendar
class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    @property
    def is_overdue(self):
        return datetime.now() > self.due_date

    def remind(self):
        status = "Просрочен" if self.is_overdue else "Активен"
        print(f"[{status}] Напоминание: {self.title} (до {self.due_date})")


def add_reminders(content_calendar, reminders_data=None):
    reminders = []
    if reminders_data:
        for title, due in reminders_data.items():
            reminders.append(Reminder(title, datetime.fromisoformat(due)))
    content_calendar.reminders = reminders
    return reminders


def show_reminders(content_calendar):
    reminders = getattr(content_calendar, 'reminders', [])
    if not reminders:
        print("Нет активных напоминаний.")
        return
    for r in reminders:
        r.remind()
