from .models import Bandas, Artistas, Musicas
from .serializers import BandasSerializer, ArtistasSerializer, MusicasSerializer
from rest_framework import viewsets

# Viewset dos artistas
class ArtistasViewSet(viewsets.ModelViewSet):
    queryset = Artistas.objects.all()
    serializer_class = ArtistasSerializer


# Viewset das bandas
class BandasViewSet(viewsets.ModelViewSet):
    queryset = Bandas.objects.all()
    serializer_class = BandasSerializer
    # http_method_names = ['get']


# Viewset das músicas
class MusicasViewSet(viewsets.ModelViewSet):
    queryset = Musicas.objects.all()
    serializer_class = MusicasSerializer
