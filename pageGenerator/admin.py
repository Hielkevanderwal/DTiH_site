from django.contrib import admin

from .models import Raw_ppg_data, Processed_ppg_data, CDSModel, ADSModel, AccesTo, DocterOf
# Register your models here.

class RawPpgDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'processed')
admin.site.register(Raw_ppg_data, RawPpgDataAdmin)

class CDSAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'score')
admin.site.register(CDSModel, CDSAdmin)

class ADSAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'score')
admin.site.register(ADSModel, ADSAdmin)

admin.site.register(Processed_ppg_data)
admin.site.register(AccesTo)
admin.site.register(DocterOf)