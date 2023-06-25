from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from main.models import UnitsModel
from main.serializers import UnitsModelSerializer


def index(request):
    return render(request, 'main/index.html')


class UnitsModelView(ModelViewSet):
    queryset = UnitsModel.objects.all()
    serializer_class = UnitsModelSerializer

