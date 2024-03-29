# Generated by Django 4.1.4 on 2024-02-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_review_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='facebook',
            field=models.URLField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='instagram',
            field=models.URLField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='keywords',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='site',
            name='twitter',
            field=models.URLField(blank=True, max_length=120, null=True),
        ),
    ]
