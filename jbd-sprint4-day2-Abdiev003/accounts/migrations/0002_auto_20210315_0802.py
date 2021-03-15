# Generated by Django 3.1.7 on 2021-03-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.BooleanField(choices=[(True, 'Men'), (False, 'Woman')], default=False, verbose_name='Gender'),
        ),
    ]