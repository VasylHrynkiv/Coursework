from django.contrib import admin
from .models import Developer, Package, Gen_info

admin.site.register(Developer)
admin.site.register(Package)
admin.site.register(Gen_info)