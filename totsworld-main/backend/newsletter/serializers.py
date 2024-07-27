from rest_framework import serializers
from .models import Newsletter

# Serializers define the API representation.
class NewsletterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Newsletter
        fields = ["pk","email","subscription_status","created_at","updated_at"]