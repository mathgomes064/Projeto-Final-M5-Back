# Generated by Django 4.0.7 on 2023-01-05 14:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('service_description', models.CharField(max_length=50)),
                ('service_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('atuation_area', models.CharField(max_length=50)),
            ],
        ),
    ]
