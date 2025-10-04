from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated 
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .permision import IsOwnerOrAdmin
from .paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrAdmin] 
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['buy_price', 'sell_price','created_at']
    search_fields = ['title']
    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_staff:
            return Product.objects.all()
        return Product.objects.filter(user=user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)