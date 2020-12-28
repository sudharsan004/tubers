from django.contrib import admin
from .models import *
# Register your models here.


class ContactTuberAdmin(admin.ModelAdmin):
    def youtuber_name(self, object):
        return object.ytuber_contacted.name
    list_display = ('first_name', 'email', 'youtuber_name')


admin.site.register(ContactInfo, ContactTuberAdmin)
