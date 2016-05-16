from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/tags/%s' % (self.id)


class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/questions/%s' % (self.id)


class Answer(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    is_better = models.BooleanField()
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return '/answers/%s' % (self.id)


class Vote(models.Model):
    answer = models.ForeignKey(Answer)
    who = models.ForeignKey(User)
    type = models.CharField(max_length=1)

    def __str__(self):
        res = "%s gave to a %s\'s answer a " % (self.who.username, self.answer.question.title)
        if self.type == 'U':
            res += "+1"
        else:
            res += "-1"
        return res

    def get_absolute_url(self):
        return '/votes/%s' % self.id
