from django.db import models
from djmoney.models.fields import MoneyField
import datetime

# Create your models here.
class Expense(models.Model):
    id = models.BigAutoField(primary_key=True)
    expense = models.CharField(max_length=250, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency="RWF", null=False, blank=False)
    date = models.DateField(default=datetime.datetime.now())

    class Meta:
        ordering =["date"]
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return self.expense


