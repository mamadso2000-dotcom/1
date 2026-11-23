from django.contrib import admin
from .models import Project, ProjectImage

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_status', 'start_date', 'end_date')

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)