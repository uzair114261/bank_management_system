from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView, DestroyAPIView
from .serializers import UserSerializer
from ..models import User
from django.db import IntegrityError

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)


class SignupView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            User.objects.create_user(username=username, password=password, email=email)
            return Response({
                "success": True,
                "message": "User created successfully"
            }, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response({
                "success": False,
                "message": "Username already exists"
            }, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response({
            'success': True,
            'message': 'Logout Successfully'
        }, status=status.HTTP_200_OK)

class UserOperations(APIView):
    serializer_class = UserSerializer
    def get_user(self, username):
        return User.objects.filter(username=username).first()

    def patch(self, request, username):
        user = self.get_user(username)
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        if user:
            if first_name is not None:
                user.first_name = first_name
            if last_name is not None:
                user.last_name = last_name
            if email is not None:
                user.email = email
            user.save()
            return Response({
                "data": "User updated"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "data": "User not found"
            }, status=status.HTTP_404_NOT_FOUND)


    def get(self, request, username):
        user = self.get_user(username)
        serializer = UserSerializer(user)
        if user:
            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "data": "Not found"
            }, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, username):
        user = self.get_user(username)
        if user:
            user.delete()
            return Response({
                "data": "Deletion Successful"
            },status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({
                "data": "Not found"
            }, status=status.HTTP_404_NOT_FOUND)



class UserDelete(DestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_object(self):
        username = self.kwargs['username']
        return User.objects.get(username=username)