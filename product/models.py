from django.db import models


class Product(models.Model):
    title=models.CharField(max_length=255)
    buy_price=models.FloatField()
    sell_price=models.FloatField()
    quantity=models.IntegerField()
    user=models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
