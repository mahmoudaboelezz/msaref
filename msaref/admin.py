from django.contrib import admin
from .models import Section, Total, Paid, Band
# Register your models here.

# class band stacked inline
class BandInline(admin.StackedInline):
    model = Band
    extra = 1

class PaidAdmin(admin.ModelAdmin):
    list_display = ('name', 'section','band_elm', 'price', 'paid_up', 'residual', 'done')
    list_filter = ('section', 'done')
    search_fields = ('name', 'section')
    list_editable = ('paid_up', 'done', 'band_elm')
    list_per_page = 20
    
    inlines = [BandInline]
    extra = 1
    

class TotalAdmin(admin.ModelAdmin):
    list_display = ('Total', 'residual_total', 'overall_total', 'section', 'updated')
    list_filter = ('section',)
    search_fields = ('section',)
    list_per_page = 20
    ordering = ('-residual_total','section')
    
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'section',  'get_total_paid', 'get_total_residual', 'get_total')
    list_filter = ('section',)
    search_fields = ('name', 'section')
    list_per_page = 20
    ordering = ('section',)
    readonly_fields = ('get_total_paid','get_total_residual', 'get_total')
    
    def get_total_paid(self, obj):
        print(obj)
        print(obj.get_total_paid())
        return obj.get_total_paid()
    
    get_total_paid.short_description = 'Total Paid'
    
    def get_total_residual(self, obj):
        return obj.get_total_residual()
    
    get_total_residual.short_description = 'Total Residual'
    
    def get_total(self, obj):
        return obj.get_total()
    
    get_total.short_description = 'Total'




admin.site.register(Section)
admin.site.register(Total, TotalAdmin)
admin.site.register(Paid, PaidAdmin)
admin.site.register(Band, BandAdmin)