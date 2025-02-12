from django.contrib import admin

from Auth.models import Admin , Employe , SousAdmin

# Register your models here.
admin.site.register(Admin)
admin.site.register(Employe)
admin.site.register(SousAdmin)