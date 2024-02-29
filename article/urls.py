from django.urls import path

from article.api.controllers.article_controller import ArticlesController

urlpatterns = [
    path('articles', ArticlesController.as_view(), name='articles'),
]