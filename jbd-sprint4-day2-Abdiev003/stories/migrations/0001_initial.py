# Generated by Django 3.1.7 on 2021-03-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=127, verbose_name='Tam adi')),
                ('email', models.EmailField(max_length=63, verbose_name='E-poct')),
                ('subject', models.CharField(max_length=255, verbose_name='Movzu')),
                ('message', models.TextField(verbose_name='Mesaj')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Basliq')),
                ('short_description', models.CharField(max_length=255, verbose_name='Qisa Mezmun')),
                ('image', models.ImageField(upload_to='recipe_images', verbose_name='Sekil')),
                ('category', models.IntegerField(choices=[(1, 'Dessert'), (2, 'Salat'), (3, 'Xalodni')], verbose_name='Kategoriya')),
                ('description', models.TextField(verbose_name='Mezmun')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
