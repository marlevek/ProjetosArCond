from django.contrib import admin

# Register your models here.
from . models import Instalacao

class InstalacaoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'tipo', 'tecnologia', 'capacidade', 'cliente', 'valor_instal']
    search_fields = ['marca', 'tipo', 'tecnologia', 'capacidade', 'fluido']
    list_filter = ['tecnologia']


admin.site.register(Instalacao, InstalacaoAdmin)