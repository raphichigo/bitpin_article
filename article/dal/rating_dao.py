from article.dal.article_dao import ArticleDao
from article.models import Rating, Article


class RatingDao:
    def __init__(self):
        self.article_dao = ArticleDao()

    def rate_to_post(self, article, user, rate: int):
        return Rating.objects.create(rater=user, rate=rate, article=article)

    def if_rate_already_exist(self, article: Article, user, ):
        return Rating.objects.filter(rater=user, article=article).exists

    def update_rate_to_post(self, article: Article, user, rate: int):
        rating = Rating.objects.filter(rater=user, article=article).first()
        rating.rate = rate
        rating.save()
        return rating
