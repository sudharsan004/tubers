from django.contrib import admin
from django.utils.html import format_html
from . import models
# Register your models here.


class TeamAdmin(admin.ModelAdmin):

    def Photo(self, object):
        return format_html(f'<img width="40" style="border-radius:10" src={object.image.url}/>')

    list_display = ('id', 'Photo', 'name', 'role', 'created_at', )
    list_display_links = ('id', 'name',)
    list_filter = ('role',)
    search_fields = ('name',)


class SliderAdmin(admin.ModelAdmin):

    def Photo(self, object):
        return format_html(f'<img width="30"  src={object.image.url}/>')

    list_display = ('title', 'Photo', 'button_text')


admin.site.register(models.Slider, SliderAdmin)
admin.site.register(models.TeamMember, TeamAdmin)
