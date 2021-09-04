from rest_framework import serializers

import api.models


class TransactionsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = api.models.Transactions
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    transactions = TransactionsSerializer(many=True, required=False)
    date = serializers.ReadOnlyField()

    class Meta:
        model = api.models.Invoice
        fields = '__all__'
