from django.test import TestCase, Client
from unittest import mock

from planeta.api.viewsets import PlanetaViewset
from planeta.models import Planeta


class PlanetaTestCase(TestCase):
    def setUp(self):
        self.viewset = PlanetaViewset()
        self.planeta = Planeta.objects.create(
            nome='Tatooine', clima='Árido', terreno='Deserto'
        )
        self.content = [
            {
                'results': [
                    {
                        'films': [
                            'Uma Nova Esperança',
                            'O Império Contra Ataca',
                            'O Retorno de Jedi'
                        ]
                    }
                ]
            },
            {
                'title': 'Uma Nova Esperança'
            },
            {
                'title': 'O Império Contra Ataca'
            },
            {
                'title': 'O Retorno de Jedi'
            }
        ]

    def test_retorna_filmes_planeta(self):
        resultado = self.content[0].get('results')[0].get('films')
        planeta = Planeta.objects.get(pk=1)

        mock_requests = mock.patch('planeta.api.viewsets.requests.get')
        mock_get = mock_requests.start()
        mock_get.return_value.json.side_effect = self.content

        lst_filmes = self.viewset.get_filmes_planeta(planeta.nome)
        mock_requests.stop()

        self.assertEqual(resultado, lst_filmes)

    def test_retorna_filmes_planeta_nome_errado(self):
        resultado = ['Relação de filmes indisponível']
        self.planeta = Planeta.objects.create(
            nome='Nome Errado', clima='Árido', terreno='Deserto'
        )
        planeta = Planeta.objects.get(pk=2)

        mock_requests = mock.patch('planeta.api.viewsets.requests.get')
        mock_get = mock_requests.start()
        mock_get.return_value.json.return_value = {}

        response = self.viewset.get_filmes_planeta(planeta.nome)
        mock_requests.stop()
        self.planeta = Planeta.objects.get(pk=2).delete()

        self.assertEqual(resultado, response)

    def test_listagem_planetas(self):
        resultado = [
            {
                'id': 1,
                'nome': 'Tatooine',
                'clima': 'Árido',
                'terreno': 'Deserto',
                'filmes': [
                    'Uma Nova Esperança',
                    'O Império Contra Ataca',
                    'O Retorno de Jedi'
                ]
            }
        ]

        mock_requests = mock.patch('planeta.api.viewsets.requests.get')
        mock_get = mock_requests.start()
        mock_get.return_value.json.side_effect = self.content

        client_side = Client()
        response = client_side.get('/api/planetas/')
        mock_requests.stop()

        self.assertEqual(resultado, response.data)

    def test_detalhe_planeta(self):
        resultado = [
            {
                'id': 1,
                'nome': 'Tatooine',
                'clima': 'Árido',
                'terreno': 'Deserto',
                'filmes': [
                    'Uma Nova Esperança',
                    'O Império Contra Ataca',
                    'O Retorno de Jedi'
                ]
            }
        ]

        mock_requests = mock.patch('planeta.api.viewsets.requests.get')
        mock_get = mock_requests.start()
        mock_get.return_value.json.side_effect = self.content

        client_side = Client()
        response = client_side.get('/api/planetas/1/')
        mock_requests.stop()

        self.assertEqual(resultado[0], response.data)

    def test_busca_planeta_por_nome(self):
        resultado = [
            {
                'id': 1,
                'nome': 'Tatooine',
                'clima': 'Árido',
                'terreno': 'Deserto',
                'filmes': [
                    'Uma Nova Esperança',
                    'O Império Contra Ataca',
                    'O Retorno de Jedi'
                ]
            }
        ]

        mock_requests = mock.patch('planeta.api.viewsets.requests.get')
        mock_get = mock_requests.start()
        mock_get.return_value.json.side_effect = self.content

        client_side = Client()
        response = client_side.get('/api/planetas/?nome=Tatooine')
        mock_requests.stop()

        self.assertEqual(resultado, response.data)
