# Generated by Django 2.2.20 on 2021-05-01 17:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False)),
                ('json_data', models.CharField(blank=True, max_length=1000, null=True)),
                ('action_url', models.CharField(blank=True, max_length=500, null=True)),
                ('time', models.DateTimeField()),
                ('content', models.CharField(max_length=500, null=True)),
                ('summary', models.CharField(max_length=100)),
                ('severity', models.PositiveIntegerField(default=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
            ],
        ),
    ]
