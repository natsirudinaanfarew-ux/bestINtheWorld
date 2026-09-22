# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: ContentCalendar
class Favorites:
    def __init__(self, content_calendar):
        self._cal = content_calendar
        self._favorites = []

    def add_favorite(self, post_id):
        post = self._cal.get_post(post_id)
        if post and post_id not in self._favorites:
            self._favorites.append(post_id)
            return True
        return False

    def remove_favorite(self, post_id):
        if post_id in self._favorites:
            self._favorites.remove(post_id)
            return True
        return False

    def is_favorite(self, post_id):
        return post_id in self._favorites

    def get_favorites(self):
        return [self._cal.get_post(p) for p in self._favorites if self._cal.get_post(p)]

    def quick_access(self):
        posts = self.get_favorites()
        return posts
