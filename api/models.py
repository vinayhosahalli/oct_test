from django.db import models
from django.db.models import Sum


class Invoice(models.Model):
    customer = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    total_quantity = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calc(self):
        transactions = self.transactions.all().aggregate(Sum('quantity'), Sum('total'))
        self.total_quantity = transactions['quantity__sum'] or 0
        self.total_amount = transactions['total__sum'] or 0
        self.save()


class Transactions(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='transactions', null=True, blank=True)
    product = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
