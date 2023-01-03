import django_filters
from book.models import HotelRoomReservation, VillaReservation, FlightReservation


class HotelRoomFilterSet(django_filters.FilterSet):
    check_in = django_filters.DateFilter(field_name='check_in', lookup_expr='gte')
    check_out = django_filters.DateFilter(field_name='check_out', lookup_expr='lt')
    hotel = django_filters.CharFilter(field_name='hotel_room__hotel__title')
    price = django_filters.CharFilter(field_name='total_payment')

    class Meta:
        model = HotelRoomReservation
        fields = ()


class VillaFilterSet(django_filters.FilterSet):
    check_in = django_filters.DateFilter(field_name='check_in', lookup_expr='gte')
    check_out = django_filters.DateFilter(field_name='check_out', lookup_expr='lt')
    villa = django_filters.CharFilter(field_name='villa__title')
    total_payment = django_filters.CharFilter(field_name='total_payment')

    class Meta:
        model = VillaReservation
        fields = ()


class FlightFilterSet(django_filters.FilterSet):
    origin = django_filters.DateFilter(field_name='airplane__origin', lookup_expr='gte')
    destination = django_filters.DateFilter(field_name='airplane__destination', lookup_expr='lt')
    airplane = django_filters.CharFilter(field_name='airplane__company')
    flight_type = django_filters.CharFilter(field_name='airplane__flight_type')
    category = django_filters.CharFilter(field_name='airplane__category')
    total_payment = django_filters.CharFilter(field_name='airplane__price')

    class Meta:
        model = FlightReservation
        fields = ()

