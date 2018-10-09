from .models import Transaction
import django_filters

class TransactionFilter(django_filters.FilterSet):
    date_between = django_filters.DateFromToRangeFilter(field_name='tr_date')
    #day = django_filters.NumberFilter(field_name='tr_date', lookup_expr='day')
    #month = django_filters.NumberFilter(field_name='tr_date', lookup_expr='month')
    #year = django_filters.NumberFilter(field_name='tr_date', lookup_expr='year')
    buyer = django_filters.CharFilter(lookup_expr='icontains')
    site_code = django_filters.CharFilter(lookup_expr='icontains')
    lorry_code = django_filters.CharFilter(lookup_expr='icontains')
    supplier = django_filters.CharFilter(lookup_expr='icontains')
    short_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Transaction
        fields = ['buyer', 'site_code', 'lorry_code', 'supplier', 'short_name']
