from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Tag(models.Model):
    TAGCHOICES = (
        ('phone', 'phone'),
        ('headphone', 'headphone'),
        ('power bank', 'power bank'),
        ('laptop', 'laptop'),
        ('printer', 'printer'),
    )

    name = models.CharField(max_length=200, null=True, choices=TAGCHOICES)
    image = models.ImageField(upload_to='static/images', default='image_not_found.jpg', null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.CharField(max_length=3000, null=True)
    name = models.CharField(max_length=3000, null=True)
    bestLink = models.CharField(max_length=3000, null=True)
    price = models.CharField(max_length=10, default=0, null=True)
    image = models.CharField(max_length=3000, null=True)

    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=3000, null=True)

    def __str__(self):
        return self.name