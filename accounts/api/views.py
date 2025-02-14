from django.core.serializers import serialize
from django.template.context_processors import request
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import AccountSerializer
from ..models import Account, Bank
from rest_framework import generics
from rest_framework import viewsets

# By APIViews
class BankAccountAPIView(APIView):
    def get_bank(self, bank_id):
        try:
            return Bank.objects.get(id=bank_id)
        except Bank.DoesNotExist:
            return None

    def get(self, request):
        accounts = Account.objects.filter(user=request.user).select_related('bank', 'user')
        serializer = AccountSerializer(accounts, many=True)
        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        bank_id = request.data.get('bank_id')
        balance = request.data.get('balance')
        account_data = {
            'bank': bank_id,
            'user': request.user.id,
            'balance': balance
        }
        serializer = AccountSerializer(data=account_data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "error": serializer.errors
            },status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        bank_id = request.data.get('bank_id')
        new_balance = request.data.get('new_balance')
        bank = self.get_bank(bank_id)

        account = Account.objects.filter(
            bank=bank,
            user=request.user
        ).select_related('bank','user').first()

        if account and account.user == request.user:
            serializer = AccountSerializer(account,
                data={
                    'balance': new_balance
                },
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "Account balance updated"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "error": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "error": "You are not authorized to change the balance"
            }, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        bank_id = request.query_params.get('bank_id')
        bank = self.get_bank(bank_id)
        account = Account.objects.filter(
            user=request.user,
            bank=bank
        ).select_related('user','bank')
        if account:
            account.delete()
            return Response({
                "data": "deletion successful"
            },status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({
                "error": "No account found"
            }, status=status.HTTP_404_NOT_FOUND)


# By Generic Views
class BankAccountGenericView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = AccountSerializer
    def get_queryset(self):
        return Account.objects.filter(user=self.request.user).select_related('user','bank')

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)


# By Generic Views
class AccountActionGenericView(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    serializer_class = AccountSerializer
    lookup_field = 'bank_id'

    def get_queryset(self):
        bank_id = self.kwargs['bank_id']
        user_id = self.kwargs['user_id']
        # Get the queryset filtered by user and bank_id
        return Account.objects.filter(user=user_id, bank__id=bank_id).select_related('user','bank')


# By Viewset
class BankAccountViewSets(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)