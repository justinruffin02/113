from django.urls import path
from posts import views


urlpatterns = [
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("", views.PostListView.as_view(), name="list"),
    path("<int:pk>", views.PostDetailView.as_view(), name="detail"),
    path("create/", views.PostCreateView.as_view(), name="create"),
    path("drafts/", views.PostCreateView.as_view(), name="drafts"),
    path("archive/", views.PostCreateView.as_view(), name="archive"),
]