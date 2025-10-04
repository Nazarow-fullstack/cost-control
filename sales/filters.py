# sales/filters.py
from django_filters import rest_framework as filters
from .models import Sales

class SalesFilter(filters.FilterSet):
    
    date = filters.DateFilter(field_name='created_at', lookup_expr='date')

    
    start_date = filters.DateFilter(field_name='created_at', lookup_expr='date__gte')

   
    end_date = filters.DateFilter(field_name='created_at', lookup_expr='date__lte')

    class Meta:
        model = Sales
        fields = ['date', 'start_date', 'end_date']