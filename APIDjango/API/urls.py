from rest_framework.routers import DefaultRouter
from .views import ConcessionnaireViewSet, VoitureViewSet

router = DefaultRouter()
router.register(r'concessionnaires', ConcessionnaireViewSet, basename='concessionnaire')
router.register(r'voitures', VoitureViewSet, basename='voiture')

urlpatterns = router.urls
