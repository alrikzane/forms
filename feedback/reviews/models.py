from django.db import models

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    review_text = models.TextField()

