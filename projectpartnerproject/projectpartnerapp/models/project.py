from django.db import models
from django.db.models import F
from .owner import Owner

class Project(models.Model):

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    width = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def location_sq_footage(self):
        return self.width * self.length





