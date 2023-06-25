from rest_framework.serializers import ModelSerializer

from main.models import UnitsModel


class UnitsModelSerializer(ModelSerializer):
    class Meta:
        model = UnitsModel
        fields = ['name', 'short_name']
