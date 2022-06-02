# Generated by Django 2.2.16 on 2022-06-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(choices=[(1, 1), (2, 2)]),
        ),
        migrations.AlterField(
            model_name='title',
            name='genres',
            field=models.ManyToManyField(related_name='genres', to='reviews.Genre'),
        ),
    ]