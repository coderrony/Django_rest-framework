# Generated by Django 4.2.2 on 2023-06-30 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0006_review_avg_rating_review_number_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='avg_rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='number_rating',
        ),
    ]