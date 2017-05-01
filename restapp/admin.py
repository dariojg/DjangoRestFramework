from django.contrib import admin
from restapp.models import Autor, Libro


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    fields = ('nombre',)

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'anio')
    fields = ('titulo', 'autor', 'anio')


# Register your models here.
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
# Register your models here.
