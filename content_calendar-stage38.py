# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: ContentCalendar
import unittest

from content_calendar import (
    Calendar, Publication, Channel, Topic, Status, Idea,
)


class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        self.cal = Calendar()

    def test_publication_status_change(self):
        pub = self.cal.add_publication(
            title="Test", channel="ch", topic="t", status=Status.DRAFT,
            date="2024-01-01", idea_id=None,
        )
        pub.status = Status.PUBLISHED
        self.assertEqual(pub.status, Status.PUBLISHED)

    def test_add_duplicate_channel(self):
        ch = self.cal.add_channel("ch")
        with self.assertRaises(ValueError):
            self.cal.add_channel("ch")

    def test_add_duplicate_topic(self):
        t = self.cal.add_topic("t")
        with self.assertRaises(ValueError):
            self.cal.add_topic("t")

    def test_add_duplicate_idea(self):
        i = self.cal.add_idea("idea1")
        with self.assertRaises(ValueError):
            self.cal.add_idea("idea1")

    def test_idea_to_draft(self):
        i = self.cal.add_idea("idea1")
        self.cal.add_publication(
            title="Test", channel="ch", topic="t", status=Status.DRAFT,
            date="2024-01-01", idea_id=i.id,
        )
        i.status = Status.DRAFT
        self.assertEqual(i.status, Status.DRAFT)

    def test_empty_calendar(self):
        self.assertEqual(self.cal.publications, [])
        self.assertEqual(self.cal.channels, [])
        self.assertEqual(self.cal.topics, [])
        self.assertEqual(self.cal.ideas, [])

    def test_calendar_with_data(self):
        self.cal.add_channel("ch")
        self.cal.add_topic("t")
        self.cal.add_idea("idea1")
        pub = self.cal.add_publication(
            title="Test", channel="ch", topic="t", status=Status.DRAFT,
            date="2024-01-01", idea_id="idea1",
        )
        self.assertEqual(len(self.cal.publications), 1)


if __name__ == "__main__":
    unittest.main()
