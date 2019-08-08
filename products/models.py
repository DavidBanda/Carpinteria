from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=100)
    categories = (
        ('Baño', 'Baño'),
        ('Cocina', 'Cocina'),
        ('Comedor', 'Comedor'),
        ('Recamara', 'Recamara'),
        ('Sala', 'Sala'),
    )
    category = models.CharField(max_length=10, choices=categories, default='Baño')
    content = models.TextField()
    price = models.CharField(max_length=15)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 540 or img.width > 540:
            output_size = (540, 540)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        str1 = self.title
        temp = ''
        for s in str1:
            if s == ' ':
                s = '-'
            temp = temp + s
        return temp
