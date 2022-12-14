# Generated by Django 3.1.5 on 2022-09-13 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/kino_images/')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(default=None, max_length=150, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/kino_images/')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(default=None, max_length=150, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Kino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=144, null=True)),
                ('trailer', models.CharField(blank=True, default=None, max_length=3000, null=True)),
                ('content', models.CharField(blank=True, default=None, max_length=2000, null=True)),
                ('urlss', models.URLField(blank=True, default=None, null=True)),
                ('grade', models.FloatField(blank=True, default=None, null=True)),
                ('photo', models.ImageField(upload_to='media/kino_images/')),
                ('photo_background', models.ImageField(blank=True, null=True, upload_to='media/kino_images/')),
                ('photos', models.ImageField(blank=True, null=True, upload_to='media/kino_images/')),
                ('photos2', models.ImageField(blank=True, null=True, upload_to='media/kino_images/')),
                ('photos3', models.ImageField(blank=True, null=True, upload_to='media/kino_images/')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('time', models.BigIntegerField(blank=True, default=None, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(blank=True, default=None, related_name='author', to='home.Author')),
                ('category', models.ManyToManyField(blank=True, related_name='category', to='home.Category')),
            ],
            options={
                'verbose_name': 'Кино',
                'verbose_name_plural': 'Кино',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/kino_images/')),
                ('slug', models.SlugField(default=None, max_length=150, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Продюсер',
                'verbose_name_plural': 'Продюсеры',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Production_year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(default=None, max_length=150, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Дата выхода',
                'verbose_name_plural': 'Дата выхода',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/kino_images/')),
                ('slug', models.SlugField(default=None, max_length=150, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Сценарист',
                'verbose_name_plural': 'Сценаристы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='TrendKino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=144, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('list_kino', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_kino_trend', to='home.kino')),
            ],
            options={
                'verbose_name': 'Тренд',
                'verbose_name_plural': 'Тренды',
            },
        ),
        migrations.CreateModel(
            name='PopularKino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=144, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('list_kino', models.ManyToManyField(blank=True, related_name='list_kino_popular', to='home.Kino')),
            ],
            options={
                'verbose_name': 'Список популярного',
                'verbose_name_plural': 'Список популярного',
            },
        ),
        migrations.CreateModel(
            name='NewKino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=144, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('list_kino', models.ManyToManyField(blank=True, related_name='list_kino_new', to='home.Kino')),
            ],
            options={
                'verbose_name': 'Список нового кино',
                'verbose_name_plural': 'Список нового кино',
            },
        ),
        migrations.AddField(
            model_name='kino',
            name='producer',
            field=models.ManyToManyField(blank=True, default=None, related_name='producer', to='home.Producer'),
        ),
        migrations.AddField(
            model_name='kino',
            name='production_year',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.production_year'),
        ),
        migrations.AddField(
            model_name='kino',
            name='scenario',
            field=models.ManyToManyField(blank=True, default=None, related_name='scenario', to='home.Scenario'),
        ),
        migrations.AddField(
            model_name='kino',
            name='сountry',
            field=models.ManyToManyField(blank=True, default=None, related_name='сountry', to='home.Country'),
        ),
    ]
