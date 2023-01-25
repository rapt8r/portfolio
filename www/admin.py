from django.contrib import admin
from www.models import Skill, Project, Visitor, Entry

class EntryInline(admin.TabularInline):
    model = Entry
    readonly_fields = ('method', 'datetime','info','path')
    ordering = ('-datetime',)

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'ip', 'source', 'entries_count', 'comment')
    readonly_fields = ('pk', 'ip', 'source', 'entries_count')
    inlines = [
        EntryInline,
    ]
    def entries_count(self, obj):
        return obj.entry_set.count()



class EntryAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'method', 'datetime', 'path')


# Register your models here.

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Visitor, VisitorAdmin)
