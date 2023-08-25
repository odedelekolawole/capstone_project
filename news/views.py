from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . models import News, Category
from . serializers import NewsSerializer, CategorySerializer
import uuid

from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
# from rest_framework import IsAuthenticated



# Create your views here.
"""
A view for Category to get all the category from the database
"""
@api_view(http_method_names=["GET"])
def category(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    response = {
        "message": "All the Categories",
        "data": serializer.data
    }
    return Response(data=response, status=status.HTTP_200_OK)


"""
A view for getting/listing all the news in the database and to also post a news depending on the request method sent
"""
@api_view(["GET", "POST"])
def all(request):
    news = News.objects.all().order_by("-created")
    if request.method == "POST":
        data = request.data
        serializer = NewsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Success": "Your news was created succesfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = NewsSerializer(news, many=True)
    response = {
        "message": "All News",
        "data": serializer.data
    }
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def detail(request, id):
    if request.method == "GET":
        news = News.objects.get(id=id)
        serializer = NewsSerializer(news)
        response = {
            "Success": "Your news has been created",
            "data": serializer.data
        }        
        return Response(data=response, status=status.HTTP_200_OK)
    

    elif request.method == "PUT":
        news = get_object_or_404(News, id=id)
        data = request.data
        serializer = NewsSerializer(instance=news, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Success": "Your message has beeen updated successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        news_to_be_deleted = get_object_or_404(News, id=id)
        news_to_be_deleted.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

    


