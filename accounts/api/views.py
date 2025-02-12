from django.template.context_processors import request
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import AccountSerializer
from ..models import Account, Bank
from rest_framework.generics import RetrieveAPIView


class BankAccount(APIView):
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
        bank = self.get_bank(bank_id)
        account = Account.objects.create(
            bank=bank,
            user=request.user,
            balance=balance
        )
        data = {
            "id": account.id,
            "bank_name": account.bank.bank_name,
            "branch_name": account.bank.branch_name,
            "username": account.user.get_full_name(),
            "balance": account.balance,
            "bank": account.bank.id,
            "user": account.user.id
        }
        return Response({
            "data": data
        }, status=status.HTTP_201_CREATED)

    def patch(self, request):
        bank_id = request.data.get('bank_id')
        new_balance = request.data.get('new_balance')
        bank = self.get_bank(bank_id)

        account = Account.objects.filter(
            bank=bank,
            user=request.user
        ).select_related('bank','user').first()

        if account.user == request.user:
            account.balance = new_balance
            account.save()
            return Response({
                "data": "Account balance updated"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "You are not authorized to change the balance"
            }, status=status.HTTP_401_UNAUTHORIZED)


class AccountDetailView(RetrieveAPIView):
    serializer_class = AccountSerializer

    # By-default RetrieveAPIView do not support multiple lookup fields, will see it by tomorrow
    lookup_field = 'bank_id'
    def get_queryset(self):
        bank_id = self.kwargs['bank_id']
        user_id = self.kwargs['user_id']

        # Get the queryset filtered by user and bank_id
        return Account.objects.filter(user=user_id, bank__id=bank_id)
