from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
        

class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    # override
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # 역참조 하는거니까 이름 맘대로 하면 안됨
    comment_set = CommentSerializer(many=True, read_only=True)
    # 새로운 필드 만드는거니까 암거나 가능
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        # 결과물 출력에 영향
        # validation이 진행이 돼서 결과물 출력
        fields = '__all__'

