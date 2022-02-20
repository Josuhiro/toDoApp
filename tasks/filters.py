import django_filters
from .models import *
from django_filters import CharFilter


class TaskFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title',  lookup_expr='icontains')
    content = CharFilter(field_name='content', lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['title', 'content', 'completed']
