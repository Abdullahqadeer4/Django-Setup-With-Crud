from rest_framework import serializers
from app.models import *

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model=location
        fields=('__all__')
        
class itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=items
        fields=('__all__')        