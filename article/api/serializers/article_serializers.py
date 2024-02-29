from rest_framework import serializers


class ArticlesGetResponseSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField()
    vote_count = serializers.IntegerField()
    average_rate = serializers.FloatField()


class ArticlesGetRequestSerializer(serializers.Serializer):
    page = serializers.IntegerField()
    page_size = serializers.IntegerField()
