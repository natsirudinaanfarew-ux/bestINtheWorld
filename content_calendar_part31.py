# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: ContentCalendar
class ActiveProfileSwitcher:
    def __init__(self, profiles):
        self.profiles = profiles
        self.active_profile_name = None
    
    @property
    def active_profile(self):
        if not self.profiles or not self.active_profile_name:
            return None
        for p in self.profiles:
            if p.name == self.active_profile_name:
                return p
        return None
    
    def switch_to(self, name):
        if not self.profiles:
            raise ValueError("Нет доступных профилей")
        target = next((p for p in self.profiles if p.name == name), None)
        if not target:
            raise ValueError(f"Профиль '{name}' не найден. Доступные: {[p.name for p in self.profiles]}")
        self.active_profile_name = name
    
    def list_profiles(self):
        return [f"{p.name} ({p.email})" for p in self.profiles]


class ContentCalendarWithProfiles(ContentCalendar):
    def __init__(self, profiles=None):
        super().__init__()
        self._profile_switcher = ActiveProfileSwitcher(profiles or [])
    
    @property
    def active_profile(self):
        return self._profile_switcher.active_profile
    
    def switch_to_profile(self, name):
        if not self._profile_switcher.switch_to(name):
            raise ValueError(f"Профиль '{name}' не найден")
        print(f"[ContentCalendar] Переключение на профиль: {self._profile_switcher.list_profiles()}")
