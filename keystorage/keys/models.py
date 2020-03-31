from django.db import models
from multiselectfield import MultiSelectField


class Keys(models.Model):
    key = models.CharField(max_length=250)
    key_user = models.CharField(max_length=10)
    key_kcv = models.CharField(max_length=7)
    key_type = models.CharField(max_length=3)
    key_typeW4 = models.CharField(max_length=7)
    key_nameW4 = models.CharField(max_length=20)
    test_prod_choice = (
        ('test', 'test'),
        ('prod', 'prod'),
    )
    choice = MultiSelectField(choices=test_prod_choice)


