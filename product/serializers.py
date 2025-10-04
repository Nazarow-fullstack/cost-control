from rest_framework.serializers import ModelSerializer
from .models import Product
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'buy_price', 'sell_price', 'quantity',"user",'created_at']
        read_only_fields = ['user']