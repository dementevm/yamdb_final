from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from api_comments_reviews.models import Review
from api_comments_reviews.serializers import CommentSerializer, \
    ReviewSerializer
from api_titles_genres_categories.models import Title
from api_users.permissions import IsStaffOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsStaffOrReadOnly)

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs['review_id'],
                                   title_id=self.kwargs['title_id'])
        return review.comments.all()

    def perform_create(self, serializer):
        get_object_or_404(Review, id=self.kwargs['review_id'])
        get_object_or_404(Title, id=self.kwargs['title_id'])
        return serializer.save(author=self.request.user,
                               review_id=self.kwargs['review_id'], )


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsStaffOrReadOnly)
    ordering = ['pub_date']

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        return title.reviews.all()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user,
                               title_id=self.kwargs['title_id'])
