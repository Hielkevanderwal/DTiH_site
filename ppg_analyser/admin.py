from django.contrib import admin

from .models import Raw_ppg_data, Processed_ppg_data
# Register your models here.
class RawPpgDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'processed')
admin.site.register(Raw_ppg_data, RawPpgDataAdmin)

class ProccesedPPGAdmin(admin.ModelAdmin):
    list_display = ('user', 'rmssd', 'pnn50', 'lfhf')

admin.site.register(Processed_ppg_data, ProccesedPPGAdmin)