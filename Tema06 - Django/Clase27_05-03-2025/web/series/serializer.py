from rest_framework import serializers
from . models import Category, Serie

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','description')

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Serie
        fields='__all__'
