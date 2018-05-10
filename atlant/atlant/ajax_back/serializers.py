from rest_framework import serializers
from .models import Info

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('id', 'name', 'description', 'image')
