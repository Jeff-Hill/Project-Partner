from django.db import models

class Tool(models.Model):


    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    own = models.BooleanField()
    image = models.ImageField(upload_to='images/', null=True, blank=True, max_length=300, height_field='url_height', width_field='url_width')

    def __str__(self):
        return self.name






