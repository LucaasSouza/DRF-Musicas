from .models import Artistas, Bandas, InstrumentosMusicais, GenerosMusicais, Musicas
from rest_framework import serializers

# Serializers dos instrumentos
class InstrumentosMusicaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstrumentosMusicais
        fields = '__all__'


# Serializers das pessoas/elenco
class ArtistasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artistas
        fields = '__all__'


# Serializers das pessoas/elenco
class GenerosMusicaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerosMusicais
        fields = '__all__'


# Serializers das bandas
class BandasSerializer(serializers.ModelSerializer):
    elenco = ArtistasSerializer(many=True, read_only=True)

    class Meta:
        model = Bandas
        fields = ('__all__')


# Serializers das músicas
class MusicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicas
        fields = '__all__'