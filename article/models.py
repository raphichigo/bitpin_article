from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    def __str__(self):
        return self.title


class Rating(models.Model):
    article = models.ForeignKey(Article, related_name='ratings', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField()
    rater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rates')

    def __str__(self):
        return f"{self.rate} from {self.rater} for {self.article}"

