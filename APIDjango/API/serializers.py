from rest_framework import serializers
from .models import Concessionnaire, Voiture

class ConcessionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionnaire
        fields = '__all__'
        extra_kwargs = {
            'numero_siret': {'write_only': True},
        }


class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = '__all__'
