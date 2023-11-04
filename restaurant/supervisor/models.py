from django.db import models
from table_sessions.models import Tables
from menu.models import Order

class InstantOrders(models.Model):
    table = models.CharField(max_length=10)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)


