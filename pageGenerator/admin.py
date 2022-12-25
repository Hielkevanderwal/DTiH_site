from django.contrib import admin

from .models import AccesTo, DocterOf, ScoreModel
# Register your models here.

class ScoreModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'value')
admin.site.register(ScoreModel, ScoreModelAdmin)

class AccesToAdmin(admin.ModelAdmin):
    list_display = ('user', 'ADS', 'CDS')
admin.site.register(AccesTo, AccesToAdmin)

class DocterOfAdmin(admin.ModelAdmin):
    list_display = ('docter', 'patients')
admin.site.register(DocterOf, DocterOfAdmin)