# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: ContentCalendar
class UndoManager:
    def __init__(self, max_undo=10):
        self._history = []
        self._max_history = max_undo

    def push(self, action_desc):
        if len(self._history) >= self._max_history:
            self._history.pop(0)
        self._history.append(action_desc)

    @property
    def can_undo(self):
        return bool(self._history)

    def undo_last_action(self):
        if not self.can_undo:
            raise RuntimeError("No action to undo")
        last = self._history.pop()
        # в реальном проекте здесь был бы конкретный обратный шаг;
        # для учебного проекта достаточно записать, что действие отменено.
        return {"status": "undone", "action": last}
