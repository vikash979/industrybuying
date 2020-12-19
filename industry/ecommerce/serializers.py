from rest_framework import serializers
from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id','category_name',)



class ProductSerializer(serializers.ModelSerializer):
	category = CategorySerializer(many=False)
	class Meta:
		model = Product
		fields = '__all__'

