from rest_framework import routers

from planeta.api.viewsets import PlanetaViewset

planeta_router = routers.DefaultRouter()
planeta_router.register('planetas', PlanetaViewset)