from rest_framework import serializers
from .models import Category

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = 
        fields = ['pk','name','updated_at']