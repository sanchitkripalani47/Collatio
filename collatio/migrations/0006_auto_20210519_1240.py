# Generated by Django 3.0.5 on 2021-05-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collatio', '0005_auto_20210516_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='detailPageLink',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
