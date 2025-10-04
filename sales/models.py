from django.db import models

class Sales(models.Model):
    product_id=models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity=models.IntegerField()
    user=models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.product_id} - Quantity: {self.quantity} by {self.user.username}"
