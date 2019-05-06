from Province.models import Canton,Distric
from rest_framework import  serializers;

class CantonSerializer(serializers.Serializer):
    class Meta:
        model = Canton
        fields = ('province', 'name', 'code')


class DistricSerializer(serializers.ModelSerializer):
    distric_canton = CantonSerializer(read_only=True)
    class Meta:
        model = Distric
        fields = ('province', 'distric_canton', 'name','code')
        depth = 1
    def create(self, validated_data):
        distric = Distric(
            province=validated_data['province'],
            canton=validated_data['distric_canton'],
            name=validated_data['name'],
            code = validated_data['code']
        )
        distric.save()
        return distric

       