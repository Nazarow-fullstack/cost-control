from django.shortcuts import render
from rest_framework import viewsets
from .models import Products
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated as isAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .permision import IsOwnerOrAdmin



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [isAuthenticated,IsOwnerOrAdmin] 
    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_staff:
            return Products.objects.all()
        return Products.objects.filter(user=user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


        

