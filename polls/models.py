import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

# TODO: add human-readable firld name.

class Question(models.Model):
    question_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self) -> str:
        return self.question_text
    
    # チェックアイコン画像表示
    @admin.display(
            boolean=True,
            ordering='pub_date',
            description='さいきん公開?',
    )
    def was_published_recently(self):
        now = timezone.now()
        yesterday = now - datetime.timedelta(days=1)
        return  yesterday <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
