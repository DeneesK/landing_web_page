from django.contrib import admin
from .models import CmsSlider
# Register your models here.
class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css')
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)

admin.site.register(CmsSlider, CmsAdmin)