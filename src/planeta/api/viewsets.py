from rest_framework import viewsets

from planeta.models import Planeta
from planeta.api.serializers import PlanetaSerializer

class PlanetaViewset(viewsets.ModelViewSet):
    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer