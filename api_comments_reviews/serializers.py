from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ValidationError

from api_comments_reviews.models import Comment, Review, Title


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date',)
        model = Comment


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    score = serializers.IntegerField(min_value=1, max_value=10)

    def validate(self, data):
        action = self.context['view'].action
        if action == 'create':
            author = self.context['request'].user
            title = get_object_or_404(
                Title, id=self.context['view'].kwargs['title_id'])
            if title.reviews.filter(author=author).exists():
                raise ValidationError("You can't review same title twice")
        return super(ReviewSerializer, self).validate(data)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date',)
        required_fields = ('text', 'score')
        read_only_fields = ('id', 'author')
        model = Review
