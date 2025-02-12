from rest_framework import serializers
from ..models import Account

class AccountSerializer(serializers.ModelSerializer):
    def get_username(self, obj):
        return obj.user.get_full_name()
    bank_name = serializers.ReadOnlyField(source='bank.bank_name', read_only=True)
    branch_name = serializers.ReadOnlyField(source='bank.branch_name', read_only=True)
    username = serializers.SerializerMethodField("get_username")
    class Meta:
        model = Account
        fields = "__all__"
