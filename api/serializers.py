from rest_framework import serializers
from map.models import Article


class ArticlePreviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'announce_text',
            'url',
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = [
            'title',
            'text',
            'start_date',
            'end_date',
        ]
