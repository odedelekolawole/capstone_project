from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from . models import News2, Category2
from . serializers import News2Serializer, Category2Serializer
from rest_framework.permissions import (IsAuthenticated,
                                        AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions,
                                        DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions)
from rest_framework.decorators import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from . permissions import ReadOnly, AuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_yasg.utils import swagger_auto_schema



"""
Start: Section reposible for listing/creating any news categories in the database starts here.
"""

class Category2ListCreateView(APIView):
    serializer_class = Category2Serializer


    # permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_summary="List all news")
    def get(self, request:Request, *args, **kwargs):
        category = Category2.objects.all().order_by("-id")
        serializer = self.serializer_class(category, many=True)
        response = {
            "Success": "You are seeing all the categories on this page in their reversed order of creation",
            "data": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    """
    This section is only retricted to the staff, so that nonsense category won't be added by randon user
    """
    
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Success": "Another category of news added successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""
Ends: Section reposible for listing/creating all the news categories in the database ends here.
"""

"""
Start: The section is responsible for RETRIEVING, UPDATING and DELETING news category.
"""

class Category2RetrieveUpdateDeleteView(APIView):

    """
    This endpoint is responsible for RETRIEVING a category of news from the news category
    """

    permission_classes = [IsAuthenticated]
    serializer_class = Category2Serializer
    def get(self, request, id):
        category = get_object_or_404(Category2, id=id)
        serializer = self.serializer_class(category)
        response = {
            "Success": "Your requested news with the UUID was retrieved successfully",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_201_CREATED)
    

    
    """
    This endpoint is responsible for UPDATING a category of news from the news category
    """
    permission_classes = [IsAuthenticated]
    def put(self, request, id):
        category = get_object_or_404(Category2, id=id)
        data = request.data
        serializer = self.serializer_class(category, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Success": "You news has been updated successfuly",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    """
    This endpoint is responsible for DELETING a category of news from the news category
    """

    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        news = get_object_or_404(Category2, id=id)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
"""
Ends: The section for responsible for RETRIEVING, UPDATING and DELETING news category ends here.
"""


"""
BREAK BREAK BREAK   BREAK BREAK BREAK   BREAK   BREAK   BREAK   BREAK   BREAK   BREAK   BREAK   BREAK   BREAK   BREAK   BREAK   BREAK   BREAK
Entering the News section
"""


"""
Start: This section is responsible for listing/getting all the news in the database and to create a new post
"""

class News2ListCreateView(APIView):
    serializer_class = News2Serializer
    pagination_classes = [PageNumberPagination]
    @swagger_auto_schema(operation_summary="List all the news in the database")
    def get(self, request:Request, *args, **kwargs):
        news = News2.objects.all().order_by("-created")
        serializer = self.serializer_class(instance=news, many=True)
        response = {
            "SUccess": "You are seeing all the news on this page",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    permission_classes = [IsAuthenticated]
    def post(self, request:Request, *args, **kwargs):
        if request.method == "POST":
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                response = {
                    "Success": "Your news has been created successfully",
                    "data": serializer.data
                }
                return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""
Ends: The section responsible for listing/getting all the news in the database ends from here
"""


"""
Start: The section responsible for RETRIEVING, UPDATING AND DELETING NEWS by UUID starts from here
"""
class News2RetrieveUpdateDeleteView(APIView):
    serializer_class = News2Serializer
    
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        news = get_object_or_404(News2, id=id)
        serializer = self.serializer_class(news)
        response = {
            "Success": "You are seeing the retrieved news here by the UUID provide",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)


    permission_classes = [IsAuthenticated]
    def put(self, request:Request, id):
        if request.method == "PUT":
            news = News2.objects.get(id=id)
            data= request.data
            serializer = self.serializer_class(news, data=data)
            if serializer.is_valid():
                serializer.save()
                response = {
                    "Message": "Your post was eddited successfully",
                    "data": serializer.data
                }
                return Response(data=response, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        news = get_object_or_404(News2, id=id)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
Ends: The section responsible for RETRIEVING, UPDATING AND DELETING NEWS by UUID endss from here
"""


"""
Section for Pagination, Search and filtering
"""

class News2ListCreateView(ListCreateAPIView):
    queryset = News2.objects.all()
    serializer_class = News2Serializer
    permission_classes = [AllowAny]
    pagination_classes = [PageNumberPagination]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ["name"]
    search_fields = ['name', 'tagline']

class Category2ListCreateView(ListCreateAPIView):
    queryset = Category2.objects.all()
    serializer_class = Category2Serializer
    permission_classes = [AllowAny]
    pagination_classes = [PageNumberPagination]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ["name"]
    search_fields = ['name', 'tagline']