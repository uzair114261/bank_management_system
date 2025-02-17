from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import AccountSerializer, AccountDetailSerializer
from ..models import Account, Bank
from rest_framework import generics
from rest_framework import viewsets

# By APIViews
class AccountAPIView(APIView):
    def get(self, request):
        accounts = Account.objects.filter(user=request.user).select_related('bank', 'user')
        print(accounts.query)
        serializer = AccountDetailSerializer(accounts, many=True)
        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "error": serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        account_id = request.data.get('account_id')
        account = Account.objects.filter(
            id=account_id
        ).select_related('bank','user').first()

        if account and account.user == request.user:
            serializer = AccountSerializer(account, data=request.data ,partial=True)
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
        account_id = request.query_params.get('account_id')
        account = Account.objects.filter(
            id=account_id
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
class CreateAccountGenericView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class ListAccountGenericView(generics.ListAPIView):
    serializer_class = AccountDetailSerializer
    lookup_field = 'user_id'
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return  Account.objects.filter(user__id=user_id).select_related('user','bank')



# By Generic Views
class AccountActionGenericView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountDetailSerializer
    lookup_field = 'id'
    def get_queryset(self):
        account_id = self.kwargs['id']
        # Get the queryset filtered by account_id
        return Account.objects.filter(id=account_id).select_related('user','bank')


# By Viewset
class BankAccountViewSets(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
