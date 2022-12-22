from django.contrib import admin

from .models import AccesTo, DocterOf, ScoreModel
# Register your models here.

admin.site.register(ScoreModel)
admin.site.register(AccesTo)

class DocterOfAdmin(admin.ModelAdmin):
    list_display = ('docter', 'patients')


admin.site.register(DocterOf, DocterOfAdmin)