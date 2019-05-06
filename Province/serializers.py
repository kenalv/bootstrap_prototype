from Province.models import Canton,Distric
from rest_framework import  serializers;

class CantonSerializer(serializers.Serializer):
    class Meta:
        model = Canton
        fields = ('province', 'name', 'code')

class DistricSerializer(serializers.Serializer):
    class Meta:
        model = Canton
        fields = ('province', 'canton', 'name','code')
        depth = 1
        