from . import views
from django.urls import path

app_name = "news2"
urlpatterns = [
    path("category/", views.Category2ListCreateView.as_view(), name="all_category"),
    path("amend/<uuid:id>/", views.Category2RetrieveUpdateDeleteView.as_view(), name="cat"),
    path("create/", views.News2ListCreateView.as_view(), name="news2"),
    path("modify/<uuid:id>/", views.News2RetrieveUpdateDeleteView.as_view(), name="news_detail"),
]