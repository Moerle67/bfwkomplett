from django.contrib import admin

# Register your models here.

from .models import Group, Grp_status

admin.site.register(Group)
admin.site.register(Grp_status)
