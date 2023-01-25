from django.contrib import admin
from www.models import Skill, Project, Visitor

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip', 'source', 'last_visit', 'last_page', 'views')
    readonly_fields = ('ip', 'info', 'source', 'views', 'last_visit', 'last_page')

# Register your models here.

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Visitor, VisitorAdmin)