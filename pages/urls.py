from django.urls import path, include
from .views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
urlpatterns = [
    path('accounts/', include('accounts.urls')),
]