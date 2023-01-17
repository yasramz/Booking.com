from rest_framework.routers import DefaultRouter

from payment.api.views import HotelRoomPaymentHistoryViewSet, VillaPaymentHistoryViewSet

router = DefaultRouter()

# Quarter Payment History Router Urls:
router.register(r'hotel-room-payment', HotelRoomPaymentHistoryViewSet, basename='hotel_room_payment')
router.register(r'villa-payment', VillaPaymentHistoryViewSet, basename='villa_payment')


urlpatterns = [

]

urlpatterns += router.urls
