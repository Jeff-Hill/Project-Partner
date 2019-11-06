from django.db import models
from .project import Owner

class Tool(models.Model):
# Set an owner Foreign Key property so you can filter data to be displayed by the user logged in


    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    own = models.BooleanField()
    image = models.ImageField(upload_to='images/', null=True, blank=True, max_length=300, height_field='url_height', width_field='url_width')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name






