# Generated by Django 3.0.3 on 2020-03-31 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keys', '0010_keys_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='keys',
            name='key_nameW4',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='keys',
            name='key_typeW4',
            field=models.CharField(default=0, max_length=7),
            preserve_default=False,
        ),
    ]
