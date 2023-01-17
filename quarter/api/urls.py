from rest_framework.routers import DefaultRouter
from quarter.api.views import *

router = DefaultRouter()

# Hotel Router Urls:
router.register(r'hotel', HotelViewSet, basename='hotel')
router.register(r'hotel/comment', HotelCommentViewSet, basename='hotel/comment')
router.register(r'hotel/rate', HotelRateViewSet, basename='hotel/rate')

# Hotel Room Router Urls:
router.register(r'hotelroom', HotelRoomViewSet, basename='hotelroom')
router.register(r'hotelroom/comment', HotelRoomCommentViewSet, basename='hotelroom/comment')
router.register(r'hotelroom/rate', HotelRoomRateViewSet, basename='hotelroom/rate')

# Villa Router urls:
router.register(r'villa', VillaViewSet, basename='villa')
router.register(r'villa/comment', VillaCommentViewSet, basename='villa/comment')
router.register(r'villa/rate', VillaRateViewSet, basename='villa/rate')


urlpatterns = [

]

urlpatterns += router.urls
