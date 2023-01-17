from rest_framework import mixins, viewsets
from payment.api.serializer import HotelRoomPaymentHistorySerializer, VillaPaymentHistorySerializer
from payment.models import HotelRoomPaymentHistory, VillaPaymentHistory


# ---------------------------------------- Payment History ViewSets ----------------------------------------------------

# Hotel Room:
class HotelRoomPaymentHistoryViewSet(mixins.CreateModelMixin,
                                     mixins.UpdateModelMixin,
                                     viewsets.GenericViewSet):

    queryset = HotelRoomPaymentHistory.objects.all()
    serializer_class = HotelRoomPaymentHistorySerializer


# Villa:
class VillaPaymentHistoryViewSet(mixins.CreateModelMixin,
                                 mixins.UpdateModelMixin,
                                 viewsets.GenericViewSet):

    queryset = VillaPaymentHistory.objects.all()
    serializer_class = VillaPaymentHistorySerializer


# ----------------------------------------------------------------------------------------------------------------------
