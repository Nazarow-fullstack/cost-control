from django.shortcuts import render
from rest_framework import viewsets
from .models import Sales
from .serializers import SalesSerializer
from rest_framework.permissions import IsAuthenticated 
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from .paginations import CustomPagination
from .permision import IsOwnerOrAdmin
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrAdmin]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        prd=Product.objects.get(id=serializer.data['product_id'])
        if prd.quantity<serializer.data['quantity']:
            return Response({"error":"Not enough stock"},status=status.HTTP_400_BAD_REQUEST)
        prd.quantity=prd.quantity-serializer.data['quantity']
        prd.save()
    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_staff:
            return Sales.objects.all()
        return Sales.objects.filter(user=user)
    



class MyfinanceView(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrAdmin]

    def get(self, request):
        user = request.user

        if user.is_staff:
            mysales = Sales.objects.all()
        else:
            mysales = Sales.objects.filter(user=user)

        date_param = request.GET.get('date', None)
        start_date_param = request.GET.get('start_date', None)
        end_date_param = request.GET.get('end_date', None)
        if date_param:
            mysales = mysales.filter(created_at__date=date_param)
        elif start_date_param and end_date_param:
            mysales = mysales.filter(created_at__date__gte=start_date_param, created_at__date__lte=end_date_param)
    
        total_revenue = 0
        total_cost = 0

        for sale in mysales:
            total_revenue += sale.quantity * sale.product_id.sell_price
            total_cost += sale.quantity * sale.product_id.buy_price
        
        total_profit = total_revenue - total_cost

        answer = {
            "total_revenue": total_revenue,
            "total_cost": total_cost,
            "total_profit": total_profit
        }

        return Response(answer, status=status.HTTP_200_OK)