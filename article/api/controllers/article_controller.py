from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticated

from article.api.serializers.article_serializers import ArticlesGetRequestSerializer, ArticlesGetResponseSerializer
from article.logic.article_logic import ArticleLogic


class ArticlesController(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.article_logic = ArticleLogic()

    @swagger_auto_schema(
        operation_summary="get all articles",
        operation_id="get_all_articles",
        responses={
            200: ...
        }

    )
    def get(self, request, *args, **kwargs):
        serialized_data = ArticlesGetRequestSerializer(data=request.query_params)
        if not serialized_data.is_valid():
            return Response("bad request", status=status.HTTP_400_BAD_REQUEST)
        page = serialized_data.validated_data.get('page')
        page_size = serialized_data.validated_data.get('page_size')

        articles = self.article_logic.get_article_list(page=page, page_size=page_size)
        serialized_articles = ArticlesGetResponseSerializer(articles)

        return Response(serialized_articles.data, status=status.HTTP_200_OK)
