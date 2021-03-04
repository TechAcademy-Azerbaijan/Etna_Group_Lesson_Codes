# Generated by Django 3.1.7 on 2021-03-04 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Title')),
                ('image', models.ImageField(upload_to='category_images', verbose_name='Image')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Order')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('order', '-created_at'),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Order')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ('order', '-created_at'),
            },
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('order', '-created_at'), 'verbose_name': 'Resept', 'verbose_name_plural': 'Reseptler'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='auth.user', verbose_name='author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Is Published'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='order',
            field=models.PositiveIntegerField(default=1, verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default='slug', max_length=155, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(help_text='Bu qutuya mesajinizi ehateli sekilde daxil edin', verbose_name='Mesaj'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_comments', to='stories.comment', verbose_name='Parent Comment')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='stories.recipe', verbose_name='Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, db_index=True, to='stories.Tag', verbose_name='Tags'),
        ),
    ]