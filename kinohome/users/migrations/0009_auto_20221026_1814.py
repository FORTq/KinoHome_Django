# Generated by Django 3.1.5 on 2022-10-26 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20221026_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorites',
            old_name='list_of_favorites',
            new_name='kino',
        ),
    ]
