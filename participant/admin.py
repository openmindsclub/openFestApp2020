from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Participant
from django.contrib.auth.models import Group

# Admin header customization 
admin.site.site_header = "Hacktoberfest Dashboard"
admin.site.site_title = "Welcome to Hacktoberfest Dashboard"
admin.site.index_title = "Welcome to this Portal"

@admin.register(Participant)
class ParticipantAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'university', 'branch', 'level')
    list_filter = ('university', 'branch', 'level','do_talk', 'do_git', 'do_fest')
    search_fields = ('first_name', 'last_name', 'email')
    pass 

# Register your models here.
admin.site.unregister(Group)