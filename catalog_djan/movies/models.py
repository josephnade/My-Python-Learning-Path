from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Film Name')
    description = models.TextField(verbose_name='Film Açıklaması')
    caption = models.CharField(max_length=50,verbose_name='Film Resmi')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Oluşturulma Tarihi')
    isPublished = models.BooleanField(default=True)
    image = models.ImageField(upload_to='img/%y')

    def __str__(self):
        return self.name

    def getImagePath(self):
        return '/img/' + self.image