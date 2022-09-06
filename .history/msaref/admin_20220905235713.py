from django.contrib import admin
from .models import Section, Total, Paid
# Register your models here.

class PaidAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'price', 'paid_up', 'residual', 'done')
    list_filter = ('section', 'done')
    search_fields = ('name', 'section')
    list_editable = ('paid_up', 'done')
    list_per_page = 20
    

class TotalAdmin(admin.ModelAdmin):
    list_display = ('Total', 'residual_total', 'overall_total', 'section', 'updated')
    list_filter = ('section',)
    search_fields = ('section',)
    list_per_page = 20
    ordering = ('-residual_total','section')
    




admin.site.register(Section)
admin.site.register(Total, TotalAdmin)
admin.site.register(Paid, PaidAdmin)