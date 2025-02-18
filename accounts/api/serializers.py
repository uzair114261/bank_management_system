from rest_framework import serializers
from ..models import Account
from banks.api.serializers import BankSerializer, Bank
from authentication.api.serializers import UserSerializer
from authentication.models import User


class AccountDetailSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    user = UserSerializer()
    class Meta:
        model = Account
        fields = ['id', 'bank', 'balance', 'user']


class AccountSerializer(serializers.ModelSerializer):
    # bank = BankSerializer()
    # user = UserSerializer()
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Account
        fields = ['id', 'bank', 'balance', 'user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        account = super().create(validated_data)
        return account
