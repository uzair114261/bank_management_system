from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import BankSerializer
from ..models import Bank
from .pagination import CustomPageNumberPagination
from rest_framework import generics

class Banks(generics.ListAPIView):
    queryset = Bank.objects.all().order_by('id')
    serializer_class = BankSerializer
    pagination_class = CustomPageNumberPagination
    def list(self, request, *args, **kwargs):
        items_per_page = request.query_params.get('items_per_page', 10)
        print(request.user)
        queryset = self.queryset
        paginator = self.pagination_class()
        paginator.page_size = int(items_per_page)
        page = paginator.paginate_queryset(queryset, request)
        serializer = BankSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class BankCreateView(generics.CreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer