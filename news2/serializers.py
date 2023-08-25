from django.db import models
from rest_framework import serializers
from . models import News2, Category2


class Category2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category2
        fields = "__all__"

class News2Serializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    class Meta:
        model = News2
        fields = "__all__"
        order = ["-created"]