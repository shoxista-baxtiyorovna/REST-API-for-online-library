# Generated by Django 5.2.1 on 2025-05-17 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, max_length=250, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=150)),
                ('published_date', models.DateField()),
                ('description', models.TextField(max_length=250)),
                ('page_count', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=100)),
                ('authors', models.ManyToManyField(related_name='books', to='catalog.author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='catalog.genre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('inventory_number', models.CharField(max_length=100, unique=True)),
                ('condition', models.CharField(choices=[('new', 'New'), ('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor')])),
                ('is_available', models.BooleanField(default=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='copies', to='catalog.book')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
