import django_filters
from .models import *

class KeysFilter(django_filters.FilterSet):
    class Meta:
        model = Keys
        # fields = '__all__'
        fields = ['key', 'key_user', 'key_kcv', 'key_type', 'choice']