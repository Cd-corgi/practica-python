from rest_framework import serializers 

from .models import puc

class pucSerializer(serializers.ModelSerializer):

    class Meta:
        model  = puc
        fields = ('__all__')