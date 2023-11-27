from django.test import TestCase

from todo.models import Task, Tag


class TestTodo(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            name="test_tag"
        )

    def test_tag_str(self):
        self.assertEqual(str(self.tag), self.tag.name)

    def test_check_task_ordering(self):
        task1 = Task.objects.create(
            content="Test task",
            is_done=False,
        )
        task1.tags.add(self.tag)
        task2 = Task.objects.create(
            content="Test task2",
            is_done=True,
        )
        task2.tags.add(self.tag)
        self.assertEqual(Task.objects.first(), task1)

    def test_tag_delete(self):
        Tag.objects.get(name=self.tag).delete()
        self.assertFalse(Tag.objects.filter(name=self.tag).exists())

    def test_task_delete(self):
        task = Task.objects.create(
            content="Test task",
            is_done=False,
        )
        task.tags.add(self.tag)
        Task.objects.get(content="Test task").delete()
        self.assertFalse(Task.objects.filter(content="Test task").exists())
