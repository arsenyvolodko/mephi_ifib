from django.db.models import Q
from django_filters import rest_framework as filters

from ifib.models import Podcasts


class PodcastsFilterSet(filters.FilterSet):

    id = filters.AllValuesMultipleFilter(
        field_name="id",
    )

    search = filters.CharFilter(
        method='filter_by_name_or_description',
        label='Поиск по названию или описанию',
    )

    def filter_by_name_or_description(self, queryset, search, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(description__icontains=value)
        )

    class Meta:
        model = Podcasts
        fields = ['search']
