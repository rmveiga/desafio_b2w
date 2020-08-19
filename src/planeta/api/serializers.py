from rest_framework import serializers

from planeta.models import Planeta

class PlanetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planeta
        fields = (
            'id', 'nome', 'clima', 'terreno'
        )