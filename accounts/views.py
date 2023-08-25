from django.shortcuts import render
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from . tokens import create_jwt_pair_for_user
# Create your views here.


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request:Request):
        data = request.data
        serializer = SignUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Success": "Success your account was created successfully",
                "data": serializer.data         
                }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):

    permission_classes = []
    def post(self, request:Request):
        email=request.data.get("email")
        password=request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "Success": "Your login was successfully",
                "token": tokens,
                # "token": user.auth_token.key # This that was commented out is resposible for Token and not for JWT the one above works for JWT
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"Message": "Invalid Email or Password"})

   
    def get(self, request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK)

