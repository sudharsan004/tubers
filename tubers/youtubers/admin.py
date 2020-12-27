from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.


class YtuberAdmin(admin.ModelAdmin):
    def photo(self, object):
        if object.image:
            return format_html(f'<img width="40" style="border-radius:10" src={object.image_url}/>')
        else:
            return format_html(f'<img width="40" style="border-radius:10" src="{object.image_url}"/>')

    list_display = ('name', 'photo', 'subscriber_count', 'is_featured')
    list_display_links = ('name',)
    search_fields = ('name', 'city')
    list_filter = ('camera_type', 'city')
    list_editable = ('is_featured',)


admin.site.register(Ytuber, YtuberAdmin)
