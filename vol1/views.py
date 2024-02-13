from .models import Artistas, Bandas, InstrumentosMusicais, GenerosMusicais ,Musicas
from .serializers import ArtistasSerializer, BandasSerializer, InstrumentosMusicaisSerializer, GenerosMusicaisSerializer, MusicasSerializer
from rest_framework import viewsets

# Viewset dos artistas
class InstrumentosMusicaisViewSet(viewsets.ModelViewSet):
    queryset = InstrumentosMusicais.objects.all()
    serializer_class = InstrumentosMusicaisSerializer


# Viewset dos artistas
class ArtistasViewSet(viewsets.ModelViewSet):
    queryset = Artistas.objects.all()
    serializer_class = ArtistasSerializer


# Viewset dos artistas
class GenerosMusicaisViewSet(viewsets.ModelViewSet):
    queryset = GenerosMusicais.objects.all()
    serializer_class = GenerosMusicaisSerializer


# Viewset das bandas
class BandasViewSet(viewsets.ModelViewSet):
    queryset = Bandas.objects.all()
    serializer_class = BandasSerializer
    # http_method_names = ['get']


# Viewset das músicas
class MusicasViewSet(viewsets.ModelViewSet):
    queryset = Musicas.objects.all()
    serializer_class = MusicasSerializer
