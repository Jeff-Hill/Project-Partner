from django.db import models
from .project import Project

class Material(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images/', null=True, blank=True, height_field='url_height', width_field='url_width')

    def __str__(self):
        return self.name

