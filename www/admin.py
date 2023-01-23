from django.contrib import admin
from www.models import Skill, Project, Visitor

class VisitorAdmin(admin.ModelAdmin):
    readonly_fields = ('ip', 'info')

# Register your models here.

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Visitor, VisitorAdmin)