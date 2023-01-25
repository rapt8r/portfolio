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
    short_desc = models.CharField(max_length=128, null=True)
    skills = models.ManyToManyField(Skill)
    image = models.FileField(upload_to='img/projects', validators=[FileExtensionValidator(allowed_extensions=['jpg'])])
    url = models.URLField(max_length=256)
    def __str__(self):
        return self.name



# Values available for Vistor model in source field.
SOURCE_VALUES = ('linkedin', 'cv')
class Visitor(models.Model):
    ip = models.CharField(max_length=32)
    last_visit = models.DateTimeField(auto_now=True)
    last_page = models.CharField(max_length=64, null=True)
    info = models.TextField(null=True)
    views = models.PositiveIntegerField(default=1)
    source = models.CharField(max_length=16, null=True, verbose_name='First visit source')
    def __str__(self):
        return self.ip
    class Meta:
        ordering = ['-last_visit']
    def clean(self):
        if self.source.lower() not in SOURCE_VALUES:
            self.source = 'n/a'