from django.views.generic import TemplateView , View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404,HttpResponse
from rest_framework import status
from rest_framework import viewsets,filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from django_filters.rest_framework import DjangoFilterBackend

from .models import Category,Product
from . import serializers
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import authentication

class CategoryViewset(viewsets.ModelViewSet):
	authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
	permission_classes = (IsAuthenticated,)
	queryset = Category.objects.all()
	serializer_class = serializers.CategorySerializer
	search_fields = ['category_name']
	filter_backends = [DjangoFilterBackend,filters.SearchFilter]
	filterset_fields = ['category_name']

	


	def create(self, request,*args, **kwargs): 
		data_error = []
		
		cat_obj = Category.objects.create(category_name=request.data.get('category_name'))
		serializer  = serializers.CategorySerializer(Category.objects.filter(id=cat_obj.id),many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)


class ProductViewset(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = serializers.ProductSerializer
	search_fields = ['product_name','category__category_name']
	filter_backends = [DjangoFilterBackend,filters.SearchFilter]
	filterset_fields = ['product_name']
	permission_classes = (IsAuthenticated,)
	authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]

	def create(self, request,*args, **kwargs): 
		data_error = []
		cat = request.data.get('category')['category_name']
		cat_id = Category.objects.get(category_name=cat).id
		prod_obj = Product.objects.create(product_name=request.data.get('product_name'),category_id=cat_id)
		serializer  = serializers.ProductSerializer(Product.objects.filter(id=prod_obj.id),many=True)
		# obj = Product.objects.latest('id')
		# print(obj)
		
		return Response(serializer.data, status=status.HTTP_200_OK)

