# Generated by Django 3.0.5 on 2021-05-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collatio', '0004_auto_20210314_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='image_not_found.jpg', null=True, upload_to='static/images'),
        ),
    ]
