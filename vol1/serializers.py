from .models import Bandas, Artistas, Musicas
from rest_framework import serializers

# Serializers das pessoas/elenco
class ArtistasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artistas
        fields = '__all__'

# Serializers das bandas
class BandasSerializer(serializers.ModelSerializer):
    artistas = ArtistasSerializer(many=True, read_only=True)

    class Meta:
        model = Bandas
        fields = ('__all__')


# Serializers das músicas
class MusicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicas
        fields = '__all__'