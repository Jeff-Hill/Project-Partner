from django.db import models
from .project import Project
from .project import Owner

class Material(models.Model):
# Create a model for a project material. Set blank=True and null=True so some properties can be initially set as NULL for future editing
# and the form fields can be left blank
# Set an owner Foreign Key property so you can filter data to be displayed by the user logged in
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, related_name='materials')
    image = models.ImageField(upload_to='images/', null=True, blank=True, height_field='url_height', width_field='url_width')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


