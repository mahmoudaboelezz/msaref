from django.contrib import admin
from .models import Section, Total, Paid
# Register your models here.

class PaidAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'price', 'paid_up', 'residual', 'done')
    list_filter = ('section', 'done')
    search_fields = ('name', 'section')
    list_editable = ('paid_up', 'done')
    list_per_page = 20


admin.site.register(Section)
admin.site.register(Total)
admin.site.register(Paid, PaidAdmin)