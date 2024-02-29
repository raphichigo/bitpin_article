from article.models import Article


class ArticleDao:
    def __init__(self):
        ...

    def get_articles(self):
        articles = Article.objects.all()
        return articles
