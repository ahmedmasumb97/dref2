from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResgistrationSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly

# Create your views here.


class ResgisterView(APIView):
   permission_classes = [AllowAny]
   def post(self,request):
       serializer = ResgistrationSerializer(data = request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Protectd(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        username = Response.user.usrname
        return Response({"message": f"Hello, {username}! You are authenticated."})