# Generated by Django 3.1.7 on 2021-03-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20210319_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(editable=False, max_length=155, verbose_name='Slug'),
        ),
    ]
