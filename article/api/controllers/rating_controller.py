from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticated

from article.errors import UserNotFound, ArticleNotFound
from article.logic.rating_logic import RatingLogic


class RatingController(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rating_logic = RatingLogic()

    @swagger_auto_schema(
        operation_summary="rate article",
        operation_id="rate_article",
        responses={
            200: "updated successfully",
            400: "bad request",
            404: "not found"
        }

    )
    def post(self, request, post_id, user_id, *args, **kwargs):
        rate = int(request.POST.get("rate"))
        try:

            self.rating_logic.rate_to_article(post_id, user_id, rate)
        except UserNotFound:
            Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)
        except ArticleNotFound:
            Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"updated_successfully"}, status=status.HTTP_200_OK)
