from article.models import Article
from django.db.models import Count, Avg


class ArticleDao:
    def __init__(self):
        ...

    def get_articles(self):
        articles = Article.objects.all()
        return articles


    def get_articles_with_rate_number_and_average_rate(self):
        articles_with_ratings = Article.objects.all().annotate(
            vote_count=Count('ratings'),
            average_rate=Avg('ratings__rate')
        )
        return articles_with_ratings

