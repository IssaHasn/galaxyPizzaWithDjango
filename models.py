from django.contrib.gis.db import models

class Pizza(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'photos/%y/%m/%d')
    description = models.CharField(max_length = 1000)
    price = models.DecimalField(max_digits = 20, decimal_places = 2)    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    person = models.CharField(max_length = 20)
    position = models.PointField()
    chois = models.CharField(max_length = 20)
    def __str__(self):
        return self.person

