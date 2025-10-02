from rest_framework.serializers import ModelSerializer
from .models import Products
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title', 'buy_price', 'sell_price', 'quantity',"user"]
        read_only_fields = ['user']