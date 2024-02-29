from rest_framework import serializers


class ArticleListItemSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField()
    vote_count = serializers.IntegerField()
    average_rate = serializers.FloatField()


class ArticlesGetResponseSerializer(serializers.Serializer):
    articles = serializers.ListSerializer(child=ArticleListItemSerializer)


class ArticlesGetRequestSerializer(serializers.Serializer):
    page = serializers.IntegerField()
    page_size = serializers.IntegerField()
