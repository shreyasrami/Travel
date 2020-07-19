from django.contrib import admin
from .models import destination

# Register your models here.


admin.site.register(destination)
admin.site.site_header = 'My administration'
admin.site.site_title = 'Travel'
admin.site.index_title = 'Site admin panel'