from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Reporter(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=255)
    content = models.TextField()
    # on_deleteはReporterが削除されたら、関連したArticleも削除
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

class Contact(models.Model):
    subject = models.TextField()
    message = models.TextField()
    sender = models.EmailField()
    pub_date = models.DateTimeField()

    created_by = models.ForeignKey(
        #get_user_model(),
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        )

    def __str__(self) -> str:
        return self.subject

class MyUser(AbstractUser):
    pass
