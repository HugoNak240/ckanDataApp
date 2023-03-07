from django.contrib import admin
from .models import StS2020toCurrent


class StS2020toCurrentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['analysis_date']}),
        ('Analytes', {'fields': ['analyte'], 'classes':['collapse']}),
    ]
    list_display = ('analyte', 'analysis_date')


admin.site.register(StS2020toCurrent, StS2020toCurrentAdmin)

# Register your models here.
