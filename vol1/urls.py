from .views import ArtistasViewSet, BandasViewSet, InstrumentosMusicaisViewSet, GenerosMusicaisViewSet, MusicasViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('instrumentos-musicais', InstrumentosMusicaisViewSet, basename='instrumentos-musicais')
router.register('generos-musicais', GenerosMusicaisViewSet, basename='generos-musicais')
router.register('artistas', ArtistasViewSet, basename='artistas')
router.register('bandas', BandasViewSet, basename='bandas')
router.register('musicas', MusicasViewSet, basename='musicas')

urlpatterns = router.urls