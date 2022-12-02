from django.contrib import admin

# Register your models here.

from restaurant.persistence.models import Cliente, Mesa, Modulo, Surcursales, Usuario, Plato

admin.site.register(Cliente)
admin.site.register(Mesa)
admin.site.register(Modulo)
admin.site.register(Surcursales)
admin.site.register(Usuario)
admin.site.register(Plato)
