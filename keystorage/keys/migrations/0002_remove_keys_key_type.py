# Generated by Django 3.0.3 on 2020-03-26 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keys',
            name='key_type',
        ),
    ]