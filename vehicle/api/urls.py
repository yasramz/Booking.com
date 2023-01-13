from rest_framework.routers import DefaultRouter
from vehicle.api.views import *

router = DefaultRouter()

router.register(r'flight', FlightViewSet, basename='flight')
router.register(r'flight/rate', FlightRateViewSet, basename='flight/rate')
router.register(r'flight/comment', FlightCommentViewSet, basename='flight/comment')


urlpatterns = [

]

urlpatterns += router.urls
