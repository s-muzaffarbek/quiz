from django.contrib.auth.models import User
from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Answer(models.Model):
    name = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Result(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_question = models.IntegerField()
    correct = models.IntegerField()


    @property
    def wrong(self):
        return self.total_question - self.correct

    @property
    def total(self):
        return (self.correct / self.total_question) * 100
