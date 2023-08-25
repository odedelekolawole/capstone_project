from . import views
from django.urls import path

app_name = "new"
urlpatterns = [
    path("", views.all, name="all"),
    path("category/", views.category, name="category"),
    path("<uuid:id>/", views.detail, name="news_detail"),
]


