from .views import BandasViewSet, ArtistasViewSet, MusicasViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('artistas', ArtistasViewSet, basename='artistas')
router.register('bandas', BandasViewSet, basename='bandas')
router.register('musicas', MusicasViewSet, basename='musicas')

urlpatterns = router.urls