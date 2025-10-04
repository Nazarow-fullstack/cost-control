from rest_framework.serializers import ModelSerializer
from .models import Sales

class SalesSerializer(ModelSerializer):
    class Meta:
        model = Sales
        fields = ['id', 'product_id', 'quantity', 'user', 'created_at']
        read_only_fields = ['user', 'created_at',]