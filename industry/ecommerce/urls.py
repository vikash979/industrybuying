from django.urls import re_path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ecommerce import views

router = DefaultRouter()
router.register(r'product', views.ProductViewset)
router.register(r'cat', views.CategoryViewset)

urlpatterns = [
    re_path('', include(router.urls)),
    ]