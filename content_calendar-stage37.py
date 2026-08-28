# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: ContentCalendar
import unittest

class TestContentCalendar(unittest.TestCase):
    
    def test_add_post(self):
        calendar = ContentCalendar()
        post = Post("Test Post", "General", "Draft", "2024-01-01")
        calendar.add_post(post)
        self.assertEqual(len(calendar.posts), 1)
        self.assertEqual(calendar.posts[0].title, "Test Post")
    
    def test_add_channel(self):
        calendar = ContentCalendar()
        channel = Channel("YouTube", "Social", "Active")
        calendar.add_channel(channel)
        self.assertEqual(len(calendar.channels), 1)
        self.assertEqual(calendar.channels[0].name, "YouTube")
    
    def test_add_topic(self):
        calendar = ContentCalendar()
        topic = Topic("Tech", "Technology", "Active")
        calendar.add_topic(topic)
        self.assertEqual(len(calendar.topics), 1)
        self.assertEqual(calendar.topics[0].name, "Tech")
    
    def test_add_status(self):
        calendar = ContentCalendar()
        status = Status("Published", "Done", "Active")
        calendar.add_status(status)
        self.assertEqual(len(calendar.statuses), 1)
        self.assertEqual(calendar.statuses[0].name, "Published")
    
    def test_add_idea(self):
        calendar = ContentCalendar()
        idea = Idea("Python Tips", "2024-01-01", "General")
        calendar.add_idea(idea)
        self.assertEqual(len(calendar.ideas), 1)
        self.assertEqual(calendar.ideas[0].title, "Python Tips")
    
    def test_add_post_to_channel(self):
        calendar = ContentCalendar()
        channel = Channel("YouTube", "Social", "Active")
        calendar.add_channel(channel)
        post = Post("Video Tutorial", "General", "Draft", "2024-01-01")
        calendar.add_post(post)
        post.add_to_channel(channel)
        self.assertEqual(len(channel.posts), 1)
        self.assertEqual(channel.posts[0].title, "Video Tutorial")
    
    def test_add_post_to_topic(self):
        calendar = ContentCalendar()
        topic = Topic("Tech", "Technology", "Active")
        calendar.add_topic(topic)
        post = Post("Tech Article", "General", "Draft", "2024-01-01")
        calendar.add_post(post)
        post.add_to_topic(topic)
        self.assertEqual(len(topic.posts), 1)
        self.assertEqual(topic.posts[0].title, "Tech Article")
    
    def test_add_post_to_status(self):
        calendar = ContentCalendar()
        status = Status("Published", "Done", "Active")
        calendar.add_status(status)
        post = Post("Published Post", "General", "Done", "2024-01-01")
        calendar.add_post(post)
        post.add_to_status(status)
        self.assertEqual(len(status.posts), 1)
        self.assertEqual(status.posts[0].title, "Published Post")

if __name__ == '__main__':
    unittest.main()
