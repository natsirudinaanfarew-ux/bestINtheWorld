# === Stage 17: Добавь группировку записей по категориям ===
# Project: ContentCalendar
class Category:
    def __init__(self, name):
        self.name = name

    @property
    def records(self):
        return [record for record in self._records]

    @classmethod
    def add(cls, category_name):
        category = cls(category_name)
        category._category_records.append(category)
        Category._categories.add(category)
        return category

    @staticmethod
    def _get_categories():
        if not hasattr(Category, '_categories'):
            Category._categories = set()
        return Category._categories

    @staticmethod
    def _get_category_records():
        categories = Category._get_categories()
        records = []
        for category in categories:
            records.extend(category._records)
        return records

    @property
    def _records(self):
        if not hasattr(Category, '_category_records'):
            Category._category_records = []
        return Category._category_records


if __name__ == "__main__":
    print("ContentCalendar - Categories Module")
