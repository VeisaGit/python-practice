from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


class Keys(models.Model):
    key = models.CharField(max_length=30)
    key_user = models.CharField(max_length=10)
    key_kcv = models.CharField(max_length=7)
    key_type = models.CharField(max_length=3)
    test_prod_choice = (
        ('test', 'test'),
        ('prod', 'prod')
    )
    choice = MultiSelectField(choices= test_prod_choice)
