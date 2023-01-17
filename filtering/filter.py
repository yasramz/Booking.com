import django_filters
from book.models import HotelRoomReservation, VillaReservation, FlightReservation
from vehicle.models import Flight
from quarter.models import HotelRoom, Villa


# --------------------------------------------- Quarter FilterSets -----------------------------------------------------

# Hotel Room:
class HotelRoomFilterSet(django_filters.FilterSet):
    title = django_filters.CharFilter('hotel__title')
    location = django_filters.CharFilter('location')
    description = django_filters.CharFilter('description')
    capacity = django_filters.CharFilter('capacity')

    class Meta:
        model = HotelRoom
        fields = ()


class HotelRoomReservationFilterSet(django_filters.FilterSet):
    check_in = django_filters.DateFilter(field_name='check_in', lookup_expr='gte')
    check_out = django_filters.DateFilter(field_name='check_out', lookup_expr='lt')
    hotel = django_filters.CharFilter(field_name='hotel_room__hotel__title')
    price = django_filters.CharFilter(field_name='total_payment')

    class Meta:
        model = HotelRoomReservation
        fields = ()


# Villa:
class VillaFilterSet(django_filters.FilterSet):
    title = django_filters.CharFilter('title')
    location = django_filters.CharFilter('location')
    description = django_filters.CharFilter('description')
    capacity = django_filters.CharFilter('capacity')

    class Meta:
        model = Villa
        fields = ()


class VillaReservationFilterSet(django_filters.FilterSet):
    check_in = django_filters.DateFilter(field_name='check_in', lookup_expr='gte')
    check_out = django_filters.DateFilter(field_name='check_out', lookup_expr='lt')
    villa = django_filters.CharFilter(field_name='villa__title')
    total_payment = django_filters.CharFilter(field_name='total_payment')

    class Meta:
        model = VillaReservation
        fields = ()


# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------------------- Vehicle FilterSets -----------------------------------------------------

# Flight:
# class FlightReservationFilterSet(django_filters.FilterSet):
#     origin = django_filters.DateFilter(field_name='airplane__origin', lookup_expr='gte')
#     destination = django_filters.DateFilter(field_name='airplane__destination', lookup_expr='lt')
#     airplane = django_filters.CharFilter(field_name='airplane__company')
#     flight_type = django_filters.CharFilter(field_name='airplane__flight_type')
#     category = django_filters.CharFilter(field_name='airplane__category')
#     total_payment = django_filters.CharFilter(field_name='airplane__price')
#
#     class Meta:
#         model = FlightReservation
#         fields = ()


class FightFilterset(django_filters.FilterSet):
    origin = django_filters.DateFilter(field_name='origin')
    destination = django_filters.DateFilter(field_name='destination')
    airplane = django_filters.CharFilter(field_name='company')
    flight_type = django_filters.CharFilter(field_name='flight_type')
    category = django_filters.CharFilter(field_name='category')
    price = django_filters.CharFilter(field_name='price', lookup_expr=['gte', 'lte'])

    class Meta:
        model = Flight
        fields = ()


# ----------------------------------------------------------------------------------------------------------------------
