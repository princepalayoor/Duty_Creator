from django.contrib import admin
from .models import stafflevel,stafftype,staff

# Register your models here.

admin.site.register(stafftype)
admin.site.register(stafflevel)
admin.site.register(staff)

