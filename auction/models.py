import os
import random
from django.db import models
from users.models import NewUser
from PIL import Image


# Create your models here.


def image_path(instance, filename):
    base_name, f_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''.join((random.choice(chars)) for _ in range(10))
    return 'product/_{randomstring}{ext}'.format(basename=base_name, randomstring=random_str, ext=f_extension)


class Product(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=image_path, default='product/placeholder.png')
    min_price = models.BigIntegerField()
    end_date = models.DateTimeField(auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        img.save(self.image.path, quality=40, optimize=True)

    def __str__(self):
        return f'{self.name}'


class Bid(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'On-- {self.product} by {self.user}'
