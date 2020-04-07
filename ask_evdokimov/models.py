from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


class UserWrap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, width_field=200, height_field=200)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class QuestionManager(models.Manager):
    def best_questions(self):
        return self.get_queryset().order_by('-rating')

    def tag_questions(self, tag):
        return self.get_queryset().filter(tags__title__contains=tag)


class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    objects = QuestionManager()
