from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=64)
    svg = models.FileField(upload_to='svg', validators=[FileExtensionValidator(allowed_extensions=['svg'])])
    visible = models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Project(models.Model):
    name = models.CharField(max_length=64)
    image = models.FileField(upload_to='img/projects', validators=[FileExtensionValidator(allowed_extensions=['jpg'])])
    url = models.URLField(max_length=256)
    def __str__(self):
        return self.name