from article.dal.article_dao import ArticleDao


class ArticleLogic:
    def __init__(self):
        self.article_dao = ArticleDao()

    def get_article_list(self):
        article_objects = self.article_dao.get_articles_with_rate_number_and_average_rate()
        articles_dicts = [
            {
                "content": article.content,
                "title": article.title,
                "author_username": article.author.username,
                "vote_count": article.vote_count,
                "average_rating": article.average_rate
            }
            for article in article_objects
        ]
        return articles_dicts
