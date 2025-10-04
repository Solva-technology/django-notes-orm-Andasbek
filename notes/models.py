from django.db import models

MAX_LENGTH = 100
MAX_LENGTH_SHORT = 50

class User(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=MAX_LENGTH)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.name}"

class Status(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_SHORT, unique=True, db_index=True)
    is_final = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=MAX_LENGTH, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Note(models.Model):
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='notes')
    categories = models.ManyToManyField(Category, blank=True, related_name='notes')

    def __str__(self):
        return f"Note by {self.author.name} on {self.created_at.strftime('%Y-%m-%d')}"
