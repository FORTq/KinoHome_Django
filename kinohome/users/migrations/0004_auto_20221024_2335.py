# Generated by Django 3.1.5 on 2022-10-24 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('users', '0003_auto_20220925_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='list_of_favorites',
        ),
        migrations.AddField(
            model_name='profile',
            name='list_of_favorites',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_user_kino_favorites', to='home.kino'),
        ),
    ]
