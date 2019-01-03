from django.db import models

class Summarizer(models.Model):

    email = models.EmailField(max_length=254)
    original = models.TextField()
    summarized = models.TextField()

    def __str__(self):
        return self.summarized
    
