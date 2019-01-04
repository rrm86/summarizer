from django.db import models
from django.utils import timezone


class Summarizer(models.Model):

    title = models.CharField(default='Old', max_length=50)
    original = models.TextField()
    summarized = models.TextField()
    date = models.DateTimeField(default=timezone.now , auto_now_add=False)

    def __str__(self):
        return self.title
