# Generated by Django 4.1.4 on 2024-02-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='url',
            field=models.URLField(blank=True, default=''),
        ),
    ]