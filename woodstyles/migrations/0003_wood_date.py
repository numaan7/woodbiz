# Generated by Django 4.2.1 on 2023-05-30 09:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('woodstyles', '0002_categorie_wood_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='wood',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
