from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Bank
from rest_framework import viewsets
from rest_framework import generics
from .serializers import  BankSerializer
from .pagination import CustomPageNumberPagination

# By generic classes
class BankListGenericView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankActionGenericView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

# BankList via viewset
class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BankSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        banks = Bank.objects.all()
        paginator = CustomPageNumberPagination()
        page = paginator.paginate_queryset(banks, request)
        serializer = BankSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)