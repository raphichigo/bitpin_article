from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticated

from article.logic.article_logic import ArticleLogic


class ArticlesController(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.article_logic = ArticleLogic()

    @swagger_auto_schema(
        operation_summary="get all articles",
        responses={
            200: ...
        }

    )
    def get(self, request, *args, **kwargs):
        # todo: serialize request
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 10))
        articles = self.article_logic.get_article_list(page=page, page_size=page_size)
        #  todo: add serializer for output
        #  todo: pagination should be done!

        return Response(articles, status=status.HTTP_200_OK)
