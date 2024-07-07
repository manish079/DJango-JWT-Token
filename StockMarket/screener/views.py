from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from Login.serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response

# Create your views here.

class Aliens(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()

    def list(self, request, *args, **kwargs):
        user = request.user;
        # print(user.id)
        # print(user.username)
        return Response({"message": "Hello, World!"})


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ghost(request):
    # if request.method != 'GET':
    #     return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    print("lllllllllll: ", request.user.email)
    return Response({"message": "Hello, World! I am Ghost!", "userId": request.user.id})