from django.contrib import admin
from backscratcher.models import Backscratcher


class AdminBackscratcher(admin.ModelAdmin):
    list_display = ('name', 'cost', 'description')


admin.site.register(Backscratcher, AdminBackscratcher)
