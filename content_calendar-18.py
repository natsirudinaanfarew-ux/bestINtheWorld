# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: ContentCalendar
class Tag:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Tag name must be a non-empty string")
        self.name = name.strip().lower()

    @property
    def is_valid(self):
        return True

    def __repr__(self):
        return f"<Tag {self.name!r}>"


class TagManager:
    _instance = None
    _tags = {}  # name -> Tag

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def reset(cls):
        cls._instance = None

    def add(self, tag):
        if not isinstance(tag, Tag):
            raise TypeError("Only Tag objects can be added")
        self._tags[tag.name] = tag
        return tag

    def remove(self, tag_name):
        if tag_name in self._tags:
            removed = self._tags.pop(tag_name)
            return removed
        return None

    def get_all_tags(self):
        return list(self._tags.values())

    def contains(self, tag_name):
        return tag_name in self._tags


class ContentCalendar:
    def __init__(self):
        self.tags_manager = TagManager()

    @staticmethod
    def validate_tag(tag):
        if not isinstance(tag, Tag) or not tag.is_valid:
            raise ValueError("Invalid tag")
        return True

    def add_tag_to_post(self, post_id, tag_name):
        tag = Tag(tag_name)
        self.tags_manager.add(tag)
        if hasattr(post, 'tags'):
            post['tags'].append(tag)
        else:
            post.setdefault('tags', []).append(tag)
        return tag

    def remove_tag_from_post(self, post_id, tag_name):
        tags = getattr(post, 'tags', [])
        removed = None
        for i, t in enumerate(tags):
            if t.name == tag_name:
                tags.pop(i)
                removed = Tag(tag_name)
                break
        return removed

    def get_post_tags(self, post_id):
        return [t.name for t in getattr(post, 'tags', [])]


# Example usage
if __name__ == "__main__":
    cal = ContentCalendar()
    post1 = {"id": 1, "title": "First Post", "status": "draft"}
    tag1 = Tag("python")
    tag2 = Tag("tutorial")

    print(cal.add_tag_to_post(post1["id"], "python"))
    print(getattr(post1, 'tags', []))
