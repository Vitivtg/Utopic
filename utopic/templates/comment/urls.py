from django.template.defaulttags import comment
from django.urls import path
from .views import (UserCreateView, UserDetailView, UserDeleteView, UserUpdateView, UserListView, CommentCreateView,
                    CommentUpdateView, CommentDeleteView, CommentDetailView)

urlpatterns = [
    path("comments/", UserListView.as_view(), name="comment_list"),
    path("comments/add", CommentCreateView(), name="comments_add"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"),
    path("comment/<int:pk>/delete", CommentDeleteView.as_view(), name="comment_delete"),
    path("comment/<int:pk>/", CommentDetailView.as_view(), name="comment_detail")
]
