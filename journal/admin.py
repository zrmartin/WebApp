from django.contrib import admin
from .models import Entry, Activity, Concert, Artist

# Register your models here.
admin.site.register(Entry)
admin.site.register(Activity)
admin.site.register(Concert)
admin.site.register(Artist)