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

    def create(self, validated_data):
        transactions = validated_data.pop('transactions', [])
        invoice = api.models.Invoice.objects.create(**validated_data)
        bulk_transactions = []
        if transactions:
            for transaction in transactions:
                if 'id' in transaction:
                    del transaction['id']
                transaction.update({'invoice': invoice, 'total': transaction.get('quantity', 0) *
                                    transaction.get('price', 0)})

                bulk_transactions.append(api.models.Transactions(**transaction))
            t = api.models.Transactions.objects.bulk_create(bulk_transactions)
            invoice.calc()
        return invoice

    def update(self, instance, validated_data):
        trans = validated_data.pop('transactions', [])
        if not trans:
            tran = instance.transactions.all()
            tran.delete()
        invoice = super(InvoiceSerializer, self).update(instance, validated_data)
        create_transactions = []
        if trans:
            for transaction in trans:
                transaction.update({'invoice': invoice, 'total': transaction.get('quantity', 0) *
                                    transaction.get('price', 0)})
                if 'id' in transaction:
                    a, b = api.models.Transactions.objects.update_or_create(id=transaction['id'], defaults=transaction)
                else:
                    create_transactions.append(api.models.Transactions(**transaction))
            api.models.Transactions.objects.bulk_create(create_transactions)
        invoice.calc()
        return invoice
