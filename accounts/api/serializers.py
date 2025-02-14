from rest_framework import serializers
from ..models import Account

class AccountSerializer(serializers.ModelSerializer):
    def get_username(self, obj):
        return obj.user.get_full_name()
    bank_name = serializers.ReadOnlyField(source='bank.bank_name', read_only=True)
    branch_name = serializers.ReadOnlyField(source='bank.branch_name', read_only=True)
    user_id = serializers.ReadOnlyField(source='user.id', read_only=True)
    username = serializers.SerializerMethodField("get_username")
    class Meta:
        model = Account
        # fields = "__all__"
        fields = ['id', 'bank', 'balance', 'bank_name','branch_name','username','user_id']


    def update(self, instance, validated_data):
        if 'balance' in validated_data:
            instance.balance = validated_data['balance']
            instance.save()
            return  instance
