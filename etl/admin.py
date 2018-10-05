from django.contrib import admin

# Register your models here.
from .models import CsvData

class CsvDataAdmin(admin.ModelAdmin):
    list_display = ['name','ipv4','mac_address']
    list_display_links = ['name',]

admin.site.register(CsvData,CsvDataAdmin)  # upper class CsvDataAdmin
#admin.site.register(CsvData)