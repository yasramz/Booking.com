from rest_framework.routers import DefaultRouter
from quarter.api.views import VillaViewSet, HotelViewSet, HotelRoomViewSet

router = DefaultRouter()

router.register(r'villa', VillaViewSet, basename='villa')
router.register(r'hotel', HotelViewSet, basename='hotel')
router.register(r'hotelroom', HotelRoomViewSet, basename='hotelroom')


urlpatterns = [

]

urlpatterns += router.urls
