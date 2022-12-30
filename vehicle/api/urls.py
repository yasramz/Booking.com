from rest_framework.routers import DefaultRouter
from vehicle.api.views import FlightViewSet

router = DefaultRouter()

router.register(r'flight', FlightViewSet, basename='flight')

urlpatterns = [

]

urlpatterns += router.urls
