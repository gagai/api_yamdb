# Generated by Django 2.2.16 on 2022-06-07 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220607_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(related_name='titles', to='reviews.Genre'),
        ),
        migrations.AlterField(
            model_name='title',
            name='сategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category'),
        ),
    ]
