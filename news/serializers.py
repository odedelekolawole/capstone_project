from django.db import models
from rest_framework import serializers
from . models import News, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    class Meta:
        model = News
        fields = "__all__"
        order = ["-created"]
