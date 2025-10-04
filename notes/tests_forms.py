from django.test import TestCase
from django.urls import reverse
from notes.models import User, Status, Category, Note

class NoteFormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(name="Тест", email="test@example.com")
        cls.st_draft = Status.objects.create(name="draft", is_final=False)
        cls.cat1 = Category.objects.create(title="Общее")
        cls.cat2 = Category.objects.create(title="Работа")

    def test_get_create_ok(self):
        r = self.client.get(reverse("note_create"))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "<form")

    def test_post_create_ok(self):
        data = {
            "text": "Новая заметка",
            "author": self.user.id,
            "status": self.st_draft.id,
            "categories": [self.cat1.id, self.cat2.id],
        }
        r = self.client.post(reverse("note_create"), data, follow=True)
        self.assertEqual(r.status_code, 200)
        n = Note.objects.latest("id")
        self.assertEqual(n.text, "Новая заметка")
        self.assertEqual(n.author, self.user)
        self.assertEqual(n.status, self.st_draft)
        self.assertEqual(set(n.categories.values_list("id", flat=True)), {self.cat1.id, self.cat2.id})

    def test_get_edit_ok(self):
        n = Note.objects.create(text="old", author=self.user, status=self.st_draft)
        r = self.client.get(reverse("note_edit", args=[n.id]))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Редактировать")

    def test_post_edit_ok(self):
        n = Note.objects.create(text="old", author=self.user, status=self.st_draft)
        data = {
            "text": "updated",
            "author": self.user.id,
            "status": self.st_draft.id,
            "categories": [self.cat1.id],
        }
        r = self.client.post(reverse("note_edit", args=[n.id]), data, follow=True)
        self.assertEqual(r.status_code, 200)
        n.refresh_from_db()
        self.assertEqual(n.text, "updated")
        self.assertEqual(set(n.categories.values_list("id", flat=True)), {self.cat1.id})

    def test_detail_404(self):
        r = self.client.get(reverse("note_detail", args=[999999]))
        self.assertEqual(r.status_code, 404)
