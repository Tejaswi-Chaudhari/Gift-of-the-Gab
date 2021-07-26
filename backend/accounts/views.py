from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, CustomerSerializer, DetailsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Customer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.conf import settings
from django.core.mail import send_mail

class CurrentUserAPIView(APIView):
    # authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = (IsAuthenticated,) 
    def get(self, request , format=None):
        serializer = CustomerSerializer(request.user)
        return Response(serializer.data)

class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            response_data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogOutAPIView(APIView):

    def post(self, request, format=None):
        try:
            refresh_token = request.data.get("refresh_token")
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserDetailsAPIView(APIView):
    serializer_class = DetailsSerializer

    def get_object(self, pk):
        try:
            obj = Customer.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Customer.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = self.serializer_class(
            customer, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

