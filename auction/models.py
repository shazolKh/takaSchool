import os
import random
from django.db import models
from users.models import NewUser


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
    # price = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image_path, default='product/placeholder.png')
    min_price = models.CharField(max_length=255)
    end_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f'{self.name}'
