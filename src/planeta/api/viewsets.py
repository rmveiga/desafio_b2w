import requests
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework import viewsets
from rest_framework.response import Response

from planeta.models import Planeta
from planeta.api.serializers import PlanetaSerializer

class PlanetaViewset(viewsets.ModelViewSet):
    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer

    def get_filmes_planeta(self, nome_planeta):
        def get_nome_filmes(filmes):
            lst_filmes = list()
            for filme in filmes:
                resp = requests.get(filme)
                lst_filmes.append(resp.json().get('title'))
            return lst_filmes

        URL_PLANETAS = f'https://swapi.dev/api/planets/?search={nome_planeta}'
        response = requests.get(URL_PLANETAS)
        planeta = response.json().get('results')
        if planeta:
            return get_nome_filmes(planeta[0].get('films'))
        return ['Relação de filmes indisponível',]

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        planetas = Planeta.objects.all()
        serializer = PlanetaSerializer(planetas, many=True)
        for i in range(serializer.data.__len__()):
            nome_planeta = serializer.data[i].get('nome')
            filmes = self.get_filmes_planeta(nome_planeta)
            serializer.data[i].update({'filmes': filmes})
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 60 * 2))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        nome_planeta = serializer.data.get('nome')
        filmes = self.get_filmes_planeta(nome_planeta)
        serializer_data = serializer.data
        serializer_data.update({'filmes': filmes})
        return Response(serializer_data)