from django.db import models
from .project import Project
from .tool import Tool

class ProjectTool(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tool_list')
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)





