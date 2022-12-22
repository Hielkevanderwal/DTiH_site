from django.contrib import admin

from .models import CDSModel, ADSModel, BMIModel

# Register your models here.
class CDSAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'score')
admin.site.register(CDSModel, CDSAdmin)

class ADSAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'score')
admin.site.register(ADSModel, ADSAdmin)

class BMIAdmin(admin.ModelAdmin):
    list_display = ('user', 'bmi')
admin.site.register(BMIModel, BMIAdmin)