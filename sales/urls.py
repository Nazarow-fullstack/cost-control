from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import SalesViewSet,MyfinanceView

router = DefaultRouter()
router.register(r'sales', SalesViewSet, basename='sale')

urlpatterns = [
    path('', include(router.urls)),
    path('myfinance/', MyfinanceView.as_view(), name='myfinance'),


]