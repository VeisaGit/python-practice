# Generated by Django 3.0.3 on 2020-03-26 10:31

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('keys', '0002_remove_keys_key_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='keys',
            name='title',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('prod', 'test'), ('prod2', 'test2')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]