from django.contrib import admin

# Register your models here.
from .models import Link,HitsDatePoint

@admin.register(Link)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('id','link','short_link','hits')

@admin.register(HitsDatePoint)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('day', 'hits','link')

# admin.site.register(Url)