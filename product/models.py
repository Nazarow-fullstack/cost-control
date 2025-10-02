from django.db import models


class Products(models.Model):
    title=models.CharField(max_length=255)
    buy_price=models.FloatField()
    sell_price=models.FloatField()
    quantity=models.IntegerField()
    user=models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)