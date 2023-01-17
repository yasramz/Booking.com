from rest_framework.routers import DefaultRouter
from book.api.views import FlightReservationViewSet, HotelRoomReservationViewSet, VillaReservationViewSet

router = DefaultRouter()

# Vehicle Router Urls:
router.register(r'flightreservation', FlightReservationViewSet, basename='flight_reservation')
# Quarter Router Urls:
router.register(r'hotelroomreservation', HotelRoomReservationViewSet, basename='hotelroom_reservation')
router.register(r'villareservation', VillaReservationViewSet, basename='villa_reservation')


urlpatterns = [

]

urlpatterns += router.urls
