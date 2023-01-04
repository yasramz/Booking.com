from rest_framework.routers import DefaultRouter
from book.api.views import FlightReservationViewSet, HotelRoomReservationViewSet, VillaReservationViewSet

router = DefaultRouter()

router.register(r'flightreservation', FlightReservationViewSet, basename='flight_reservation')
router.register(r'hotelroomreservation', HotelRoomReservationViewSet, basename='hotelroom_reservation')
router.register(r'villareservation', VillaReservationViewSet, basename='villa_reservation')


urlpatterns = [

]

urlpatterns += router.urls
