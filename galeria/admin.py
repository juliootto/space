from django.contrib import admin
from galeria.models import Fotografia


# Register your models here.
class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id','nome','legenda','categoria','data_fotografia','publicado')
    list_display_links = ('id','nome')
    search_fields = ('nome','categoria')
    list_filter = ('legenda','categoria','publicado','usuario')
    list_editable = ('categoria','publicado','data_fotografia')
    list_per_page = 10

admin.site.register(Fotografia,FotografiaAdmin)