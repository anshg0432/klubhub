from django.contrib import admin
from .models import Club,Event,Highlight,Club_follow
# Register your models here.
admin.site.register(Club)
admin.site.register(Event)
admin.site.register(Highlight)
admin.site.register(Club_follow)