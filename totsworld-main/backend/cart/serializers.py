from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = 
        fields = ['pk','updated_at']