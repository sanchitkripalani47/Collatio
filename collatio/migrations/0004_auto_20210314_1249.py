# Generated by Django 3.0.5 on 2021-03-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collatio', '0003_tag_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=models.ImageField(default='image_not_found.jpg', null=True, upload_to='static/images'),
        ),
    ]
