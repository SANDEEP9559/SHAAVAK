from django.contrib import admin

# Register your models here.
from .models import *




class RickshawAdmin(admin.ModelAdmin):
    list_display = ('destination', 'fare', 'time', 'name', 'phone')


admin.site.register(Rickshaw,RickshawAdmin)


class VanAdmin(admin.ModelAdmin):
    list_display = ('destination', 'fare', 'time', 'name', 'phone')


admin.site.register(Van,VanAdmin)

class BusAdmin(admin.ModelAdmin):
    list_display = ('destination', 'fare', 'time', 'name', 'phone')


admin.site.register(Bus,BusAdmin)
