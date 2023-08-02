# Generated by Django 4.2.2 on 2023-06-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='image_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='nutrition',
            field=models.TextField(),
        ),
    ]
