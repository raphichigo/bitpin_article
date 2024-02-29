from django.urls import path

from article.api.controllers.article_controller import ArticlesController
from article.api.controllers.rating_controller import RatingController

urlpatterns = [
    path('articles', ArticlesController.as_view(), name='articles'),
    path('rate/<int:user_id>/<int:article_id>/', RatingController.as_view(), name='rate'),
]