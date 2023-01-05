from rest_framework.routers import DefaultRouter

from payment.api.views import HotelRoomPaymentHistoryViewSet, VillaPaymentHistoryViewSet

router = DefaultRouter()

router.register(r'hotel_room_payment', HotelRoomPaymentHistoryViewSet, basename='hotel_room_payment')
router.register(r'villa_payment', VillaPaymentHistoryViewSet, basename='villa_payment')


urlpatterns = [

]

urlpatterns += router.urls
