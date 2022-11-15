from django.contrib import admin
from .models import License
from .models import Proxy
from .models import Contact
from .models import Messagebox


class LicenseAdmin(admin.ModelAdmin):
    list_display = ['key', 'date_created', 'expiry_date']


class ProxyAdmin(admin.ModelAdmin):
    list_display = ["host", "port", "username", "password"]


admin.site.register(License, LicenseAdmin)
admin.site.register(Proxy, ProxyAdmin)
admin.site.register(Contact)
admin.site.register(Messagebox)
