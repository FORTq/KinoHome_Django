# Generated by Django 4.1.3 on 2022-11-14 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_sidebar_alter_author_id_alter_category_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='photo',
        ),
    ]
