from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):
    class Meta:
        model = File

admin.site.register(File, FileAdmin)
