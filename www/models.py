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
SOURCE_VALUES = ('linkedin', 'cv', 'olx', 'pracujpl', 'linkedinmsg')
class Visitor(models.Model):
    ip = models.CharField(max_length=32, verbose_name='IP')
    comment = models.CharField(max_length=32, null=True, blank=True)
    source = models.CharField(max_length=16, verbose_name='First visit source')
    first_entry = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.ip
    def clean(self):
        #Make sure that source field is correct
        if self.source.lower() not in SOURCE_VALUES:
            self.source = 'n/a'

class Entry(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, null=True)
    method = models.CharField(choices=(('POST', 'POST'),('GET', 'GET')), max_length=8)
    datetime = models.DateTimeField(auto_now_add=True)
    info = models.TextField(null=True)
    path = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Entries'
    def __str__(self):
        return f"{self.visitor} {self.method} {self.path}"
    def set_info(self, request, visitor):
        """
        Sets the info for Entry object

        :param request: HttpRequest
        :param visitor: Visitor Object
        :return:
        """
        self.method = request.method
        self.info = request.headers
        self.path = request.path
        self.visitor = visitor