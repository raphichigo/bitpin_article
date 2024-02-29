from article.dal.article_dao import ArticleDao
from article.dal.rating_dao import RatingDao
from article.dal.user_dao import UserDao
from article.errors import ArticleNotFound, UserNotFound


class RatingLogic:
    def __init__(self):
        self.rating_dao = RatingDao()
        self.user_dao = UserDao()
        self.article_dao = ArticleDao()

    def rate_to_article(
            self,
            user_id,
            article_id,
            rate):
        user = self.user_dao.get_user_by_id(
            user_id=user_id
        )
        if not user:
            raise UserNotFound("user not found!")
        article = self.article_dao.get_article_by_id(
            article_id=article_id
        )
        if not article:
            raise ArticleNotFound("article not found!")
        else:
            if self.rating_dao.if_rate_already_exist(
                    user=user,
                    article=article
            ):
                self.rating_dao.update_rate_to_post(
                    user=user,
                    article=article,
                    rate=rate)
            else:
                self.rating_dao.rate_to_post(
                    user=user,
                    article=article,
                    rate=rate)
