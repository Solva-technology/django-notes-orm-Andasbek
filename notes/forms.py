# notes/forms.py
from django import forms
from .models import Note, User, Status, Category

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("text", "author", "status", "categories")
        widgets = {
            "text": forms.Textarea(attrs={
                "class": "form-control", "rows": 6, "placeholder": "Текст заметки"
            }),
            "author": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "categories": forms.SelectMultiple(attrs={"class": "form-select", "size": 6}),
        }
        labels = {
            "text": "Текст",
            "author": "Автор",
            "status": "Статус",
            "categories": "Категории",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # красивый порядок в выпадающих списках
        self.fields["author"].queryset = User.objects.all().order_by("name")
        self.fields["status"].queryset = Status.objects.all().order_by("name")
        self.fields["categories"].queryset = Category.objects.all().order_by("title")
        # по желанию — дефолтный статус "draft", если есть
        try:
            self.fields["status"].initial = Status.objects.get(name="draft").pk
        except Status.DoesNotExist:
            pass
