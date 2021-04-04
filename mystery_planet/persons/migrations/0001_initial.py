# Generated by Django 3.1.7 on 2021-04-04 12:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('has_died', models.BooleanField()),
                ('picture', models.CharField(blank=True, max_length=100, null=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('eye_color', models.CharField(choices=[('blue', 'Blue'), ('brown', 'Brown')], max_length=20)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('greeting', models.TextField(blank=True, null=True)),
                ('tags', models.JSONField(blank=True, null=True)),
                ('registered', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='persons.company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]